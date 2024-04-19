from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

class Zcode:
    pass

class FuncZcode(Zcode):
    def __init__(self, param = [], typ = None, body = False):
        self.param = param
        self.typ = typ
        self.body = body

class VarZcode(Zcode):
    def __init__(self, typ = None):
        self.typ = typ    

class ArrayZcode(Type):
    #* eleType: List[Type]
    #* Type ở đây có thể là Zcode, ArrayZcode
    def __init__(self, typ):
        self.typ = typ
        
class StaticChecker(BaseVisitor, Utils):
    def __init__(self,ast, ):
        self.ast = ast
        self.BlockFor = 0
        self.function = None #! hàm hiện tại đang được dùng để kiểm tra static
        self.Return = False #! kiểm tra hàm hiện tại có return hay không
        
        #! lưu danh sách các hàm dưới dạng Dict 
        self.listFunction = {
                "readNumber" : FuncZcode([], NumberType(), True),
                "readBool" : FuncZcode([], BoolType(), True),
                "readString" : FuncZcode([], StringType(), True),
                "writeNumber" : FuncZcode([NumberType()], VoidType(), True),
                "writeBool" : FuncZcode([BoolType()], VoidType(), True),
                "writeString" : FuncZcode([StringType()], VoidType(), True)
                }
        
    def check(self):
        self.visit(self.ast, [{}])
        return ""
    
    def comparType(self, LHS, RHS):
        if type(LHS) is ArrayType and type(RHS) is ArrayType:
            if (len(LHS.size) != len(RHS.size)):
                return "TMM"
            for i in range(len(LHS.size)):
                if LHS.size[i] != RHS.size[i]:
                    return "TMM"
            
            if LHS.eleType != RHS.eleType:
                return "TMM"
            return "Right Type"
        
        if LHS is not None and RHS is not None:
            if str(type(LHS)) != str(type(RHS)):
                return "TMM"
            else:
                return "Right Type"
        if LHS is None and RHS is None:
            return "CNIF"
        if LHS is None and RHS is not None:
            return "infer"
        if LHS is not None and RHS is None:
            return "infer"

    def comparListType(self, LHS, RHS):
        if len(LHS) != len(RHS):
            return False
        
        count_LHS = [0, 0, 0, 0]
        count_RHS = [0, 0, 0, 0]

        for i in LHS:
            if isinstance(i, NumberType):
                count_LHS[0] += 1
            elif isinstance(i, BoolType):
                count_LHS[1] += 1
            elif isinstance(i, StringType):
                count_LHS[2] += 1
            elif isinstance(i, ArrayType):
                count_LHS[3] += 1

        for i in RHS:
            if isinstance(i, NumberType):
                count_RHS[0] += 1
            elif isinstance(i, BoolType):
                count_RHS[1] += 1
            elif isinstance(i, StringType):
                count_RHS[2] += 1
            elif isinstance(i, ArrayType):
                count_RHS[3] += 1


        for i in range(len(count_LHS)):
            if count_LHS[i]!= count_RHS[i]:
                return False
            
        return True

    def setTypeArray(self, typeArray, typeArrayZcode):
        #* Trường hợp size khác nhau
        if typeArray.size[0] != len(typeArrayZcode.eleType):
            return False
        
        #* trường hợp bên trong array là các kiểu nguyên thủy (array 1 chiều)
           #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = typeArray.eleType
           #^ nếu    là arrayZcode : trả về False (vì 1 chiều mà bắt gán 2 chiều :) )
        """_VD 
            typeArray = arrayType([3], StringType), typeArrayZcode = ArrayZcode([VarZcode('a'), FuncZcode('foo'), ArrayZcode([VarZcode('b')])])
            index = 0 -> VarZcode('a').type = StringType
            index = 1 -> FuncZcode('foo').type = StringType
            index = 2 -> ArrayZcode([VarZcode('b')]) ->  fail -> return Flase
        """
        if len(typeArray.size) == 1:
            #TODO implement
            pass
            
            #* trường hợp bên trong array là các arrayType (array >= 2 chiều)
            #^ nếu typeArrayZcode.eleType[i] là Zcode : gán typeArrayZcode.eleType[i].typ = ArrayType(typeArray.size[1:], typeArray.eleType)
            #^ nếu typeArrayZcode.eleType[i] là arrayZcode : gọi đệ quy self.setTypeArray(ArrayType(typeArray.size[1:], typeArray.eleType),typeArrayZcode[i]) để vào bên trong xem có lỗi gì không       
            """_VD 
                typeArray = arrayType([2,3], StringType), typeArrayZcode = ArrayZcode([VarZcode('a'), FuncZcode('foo'), ArrayZcode([VarZcode('b')])])
                index = 0 -> VarZcode('a').type = arrayType([3], StringType)
                index = 1 -> FuncZcode('foo').type = arrayType([3], StringType)
                index = 2 -> đệ quy typeArray = arrayType([3], StringType), typeArrayZcode = ArrayZcode([VarZcode('b')])
                    vì typeArray  có 3 phần tử mà typeArrayZcode chỉ có 1 phần tử -> return false
            """
        else:
            pass
            #TODO implement

    def visitProgram(self, ast, param):
        #! duyệt qua các biến và hàm toàn cục
        for i in ast.decl: self.visit(i, param)
        #! sau bước này param có dạng [{biến toàn cục, hàm}]

                #No Definition
        for i in self.listFunction.keys(): 
            if self.listFunction[i].body == None:
                raise NoDefinition(i)

        #No Entry Point
        if not self.listFunction.get("main"):
            raise NoEntryPoint()
        if self.listFunction.get("main").param != [] or not isinstance(self.listFunction.get("main").typ, VoidType):
            raise NoEntryPoint()
        
    def visitVarDecl(self, ast, param):
        if param[0].get(ast.name.name) != None:
            raise Redeclared(Variable(), ast.name.name)
        
        type = ast.varType
        param[0][ast.name.name] = VarZcode(type)

        if ast.varInit is not None:
            varInit = self.visit(ast.varInit, param)
            cmp = self.comparType(varInit.typ, type)
            if cmp == "TMM":
                raise TypeMismatchInStatement(ast)
            if cmp == "CNIF":
                raise TypeCannotBeInferred(ast)
            if cmp =="infer":
                if varInit.typ is None:
                    varInit.typ = type
                else:
                    param[0][ast.name.name].typ = varInit.typ


    def visitFuncDecl(self, ast, param):
        name = ast.name.name
        found = self.listFunction.get(name)
        if found and (ast.body is None or found.body is not None):
            raise Redeclared(Function(), ast.name.name)
        elif found and found.body == None:
            found.body = True
        elif not found:
            self.listFunction[name] = FuncZcode(None, None, None)

        listParam = {} #! dạng Dict có name khi visit dùng self.visit(ast.body, [listParam] + param)
        for i in ast.param:
            if listParam.get(i.name.name) != None:
                raise Redeclared(Parameter(), i.name.name)
            listParam[i.name.name] = VarZcode(i.varType)
        
        typeParam = [] #! dạng mảng không cần name truyền agrc vào FuncZcode
        for i in ast.param:
            typeParam.append(i.varType)

        if found:
            if not self.comparListType(found.param, typeParam):
                raise Redeclared(Function(), ast.name.name)

        self.function = self.listFunction[ast.name.name]
        self.function.param = typeParam

        self.Return = False

        if ast.body:
            self.function.body = True
            self.visit(ast.body, [listParam] + param)
        
        # ! hàm này không có return
        if not self.Return and ast.body:
            #! type cũng chưa có luôn ta xác định nó VoidType
            if self.listFunction[ast.name.name].typ is None:
                self.listFunction[ast.name.name].typ = VoidType()
            #! type đã có so sánh nó với VoidType
            elif self.comparType(self.listFunction[ast.name.name].typ, VoidType()) == "TMM": 
                raise TypeMismatchInStatement(Return(None))
        

    def visitId(self, ast, param):
        found = None
        for i in param:
            if i.get(ast.name):
                return i.get(ast.name)
        raise Undeclared(Identifier(), ast.name)
        
        
    def visitCallExpr(self, ast, param):
        found = self.listFunction.get(ast.name.name)
        if not found:
            raise Undeclared(Function(), ast.name.name)
        listLHS = found.param
        listRHS = ast.args
        
        if len(listLHS) != len(listRHS):
            raise TypeMismatchInExpression(ast)
        
        for i in range(len(listRHS)):
            para = self.visit(listRHS[i], param)
            if (str(type(listLHS[i])) != str(type(para.typ))):
                raise TypeMismatchInExpression(ast)
            
        if found.typ is None:
            return found
        
        if found.typ is VoidType:
            raise TypeMismatchInExpression(ast)

        return VarZcode(found.typ)
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ xét listLHS (là method.param) và listRHS (là ast.args)
                ^ nếu len khác nhau TypeMismatchInExpression
                ^ nếu self.comparType(LHS[i], RHS[i]) -> TypeMismatchInExpression
            ^ nếu FuncZcode.typ is None thì return FuncZcode
            ^ nếu comparType(FuncZcode.typ, VoidType()) -> TypeMismatchInExpression
            ^ còn lại return FuncZcode.typ (giống phần VarZcode)
        """   


    def visitCallStmt(self, ast, param):
        found = self.listFunction.get(ast.name.name)

        if not found:
            raise Undeclared(Function(), ast.name.name)
        
        listLHS = found.param
        listRHS = ast.args


        if len(listLHS) != len(listRHS):
            raise TypeMismatchInStatement(ast)

        for i in range(len(listRHS)):
            para = self.visit(listRHS[i], param)
            if (self.comparType(listLHS[i], para.typ) == "TMM"):
                raise TypeMismatchInStatement(ast)
            
        if found.typ is None:
            return found
        
        if found.typ is VoidType:
            raise TypeMismatchInStatement(ast)
        
        return VarZcode(found.typ)
        """như CallExpr chỉ khác ở chỗ not comparType(FuncZcode.typ, VoidType()) -> TypeMismatchInStatement"""
    

    def visitIf(self, ast, param):
        expr = self.visit(ast.expr, param)
        cmp = self.comparType(expr.typ, BoolType())
        if cmp == "TMM":
            raise TypeMismatchInStatement(ast)
        elif cmp == "infer":
            expr.typ = BoolType()
        self.visit(ast.thenStmt, [{}] + param)
        """_typExpr_
            # TODO giống phần kiểm tra TypeMismatchInStatement theo nguyên lí LHS và RHS
                #^ xét typExpr và self.visit(ast.thenStmt, [{}] + param)
            ^ LHS = BoolType(), RHS = self.visit(ast.expr, param)
        """   
        #TODO implement 
        for i in ast.elifStmt:
            elifExpr = self.visit(i[0], param)
            cmp = self.comparType(elifExpr.typ, BoolType())
            if cmp == "TMM":
                raise TypeMismatchInStatement(ast)
            elif cmp == "infer":
                elifExpr.typ = BoolType()
            self.visit(i[1], [{}] + param)
        """_elifStmt_
            #TODO giống trên, LHS = BoolType()
        """   


        #TODO implement
        
        """_elseStmt_
        """            
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, [{}] + param)

        
        """
            TODO kiểm tra elseStmt
            ^ body khi visit nhớ thêm 1 tầm vực mới
        """           
     
    def visitFor(self, ast, param):
        """
            TODO giống phần kiểm tra TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
            ^ ast.name có LHS = NumberType(), RHS = .....
            ^ ast.condExpr có LHS = BoolType(), RHS = .....
            ^ ast.updExpr có LHS = NumberType(), RHS = .....
        """ 
        
        name = self.visit(ast.name, param)
        condExpr = self.visit(ast.condExpr, param)
        updExpr = self.visit(ast.updExpr, param)

        cmp = self.comparType(name.typ, NumberType())
        if cmp == "TMM":
            raise TypeMismatchInStatement(ast)
        elif cmp == "infer":
            name.typ = NumberType()
        
        cmp = self.comparType(condExpr.typ, BoolType())
        if cmp == "TMM":
            raise TypeMismatchInStatement(ast)
        elif cmp == "infer":
            condExpr.typ = BoolType()

        cmp = self.comparType(updExpr.typ, NumberType())
        if self.comparType(updExpr.typ, NumberType()) == "TMM":
            raise TypeMismatchInStatement(ast)
        elif cmp == "infer":
            updExpr.typ = NumberType()
        
        self.BlockFor += 1 #! vào trong vòng for nào anh em
        self.visit(ast.body, [{}] + param) #! tăng tầm vực mới
        self.BlockFor -= 1 #! cút khỏi vòng for nào anh em
    

    def visitReturn(self, ast, param):
        if ast.expr:
            self.Return = True
            rhs = self.visit(ast.expr, param)
            cmp = self.comparType(self.function.typ, rhs.typ)
            if cmp == "TMM":
                raise(TypeMismatchInStatement(ast))
            if cmp == "CNIF":
                raise(TypeCannotBeInferred(ast))
            if cmp == "infer":
                if self.function.typ is None:
                    self.function.typ = rhs.typ
                else:
                    rhs.typ = self.function.typ
        


    def visitAssign(self, ast, param):
        lhs = self.visit(ast.lhs, param)
        rhs = self.visit(ast.rhs, param)
        cmp = self.comparType(lhs.typ, rhs.typ)
        if cmp == "TMM":
            raise TypeMismatchInStatement(ast)
        if cmp == "CNIF":
            raise TypeCannotBeInferred(ast)
        if cmp =="infer":
            if lhs.typ is None:
                lhs.typ = rhs.typ
            else:
                rhs.typ = lhs.typ
        """
            TODO giống phần kiểm tra TypeCannotBeInferred và TypeMismatchInStatement xử lí ast.varInit nếu tồn tại
        """

            

    def visitBinaryOp(self, ast, param):
        op = ast.op
        LHS = self.visit(ast.left, param)

        if op in ['+', '-', '*', '/', '%']:
            lcmp = self.comparType(LHS.typ, NumberType())
            if lcmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif lcmp == "infer":
                LHS.typ = NumberType()
            RHS = self.visit(ast.right, param)
            rcmp = self.comparType(RHS.typ, NumberType())
            if rcmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif rcmp == "infer":
                RHS.typ = NumberType()
            return VarZcode(NumberType())
        
        elif op in ['=', '!=', '<', '>', '>=', '<=']:
            lcmp = self.comparType(LHS.typ, NumberType())
            if lcmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif lcmp == "infer":
                LHS.typ = NumberType()
            RHS = self.visit(ast.right, param)
            rcmp = self.comparType(RHS.typ, NumberType())
            if rcmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif rcmp == "infer":
                RHS.typ = NumberType()
            return VarZcode(BoolType())
        
        elif op in ['and', 'or']:
            lcmp = self.comparType(LHS.typ, BoolType())
            if lcmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif lcmp == "infer":
                LHS.typ = BoolType()
            RHS = self.visit(ast.right, param)
            rcmp = self.comparType(RHS.typ, BoolType())
            if rcmp == "TMM":
                raise TypeMismatchInExpression(ast)            
            elif rcmp == "infer":
                RHS.typ = BoolType()
            return VarZcode(BoolType())
        
        elif op in ['==']:
            lcmp = self.comparType(LHS.typ, StringType())
            if lcmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif lcmp == "infer":
                LHS.typ = StringType()
            RHS = self.visit(ast.right, param)
            rcmp = self.comparType(RHS.typ, StringType())
            if rcmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif rcmp == "infer":
                RHS.typ = StringType()
            return VarZcode(BoolType())
        
        elif op in ['...']:
            lcmp = self.comparType(LHS.typ, StringType()) 
            if lcmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif lcmp == "infer":
                LHS.typ = StringType()
            rcmp = self.comparType(RHS.typ, StringType())
            if rcmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif rcmp == "infer":
                RHS.typ = StringType()
            return VarZcode(StringType())
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ visit left và right của BinaryOp
            ^ ['+', '-', '*', '/', '%'] -> kiểu numbertype -> return Numbertype
              ^ nếu left và right đề có type -> kiểm tra nén lỗi TypeMismatchInExpression
              ^ nếu in trong 2 left và right đề có type -> kiểm tra nén lỗi TypeMismatchInExpression và gán type left/right
              ^ nếu cả 2 left và right là kiểu Zcode -> gán type left và right
            ^ ['=', '!=', '<', '>', '>=', '<='] -> kiểu numbertype -> return Numbertype
            ^ ['and', 'or'] -> kiểu booltype -> return booltype
            ^ ['=='] -> kiểu stringtype -> return booltype
            ^ ['...'] -> kiểu stringtype -> return stringtype
            
            ^ gợi ý ['+', '-', '*', '/', '%']
                ^ b + c
                ^ xét đầu tiên là LHS_b = NumberType, RHS_b = self.visit(b)
                ^ xét đầu tiên là LHS_c = NumberType, RHS_c = self.visit(c)
                ^ return NumberType
                
        """        
        
  

    def visitUnaryOp(self, ast, param):
        op = ast.op
        operand = self.visit(ast.operand, param)
        if op in ['+', '-']:
            cmp = self.comparType(operand.typ, NumberType())
            if cmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif cmp == "infer":
                operand.typ = NumberType()
            return VarZcode(NumberType())
        elif op in ['not']:
            cmp = self.comparType(operand.typ, BoolType())
            if cmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif cmp == "infer":
                operand.typ = BoolType()
            return VarZcode(BoolType())
        """
            TODO giống phần kiểm tra TypeMismatchInExpression xử lí ast.varInit nếu tồn tại
            ^ visit ast.operand của UnaryOp
            ^ '+', '-' -> kiểu numbertype -> return Numbertype
            ^ ['not'] -> kiểu booltype -> return booltype
        """       


    def visitArrayCell(self, ast, param):
        """
            TODO kiểm tra TypeMismatchInExpression
            ^ Phần type ast.arr phải là array type nếu không lỗi TypeMismatchInExpression
        """ 
        left = self.visit(ast.arr, param)
        if type(left.typ) is not ArrayType:
            raise TypeMismatchInExpression(ast)
        
        for item in ast.idx:
            LHS = self.visit(item, param)
            cmp = self.comparType(LHS.typ, NumberType()) 
            if cmp == "TMM":
                raise TypeMismatchInExpression(ast)
            elif cmp == "infer":
                LHS.typ = NumberType()
        """
            # TODO kiểm tra TypeMismatchInExpression
            #* giống mấy thằng trong if
            ^ từng phần tử trong ast.idx với LHS = NumberType(), RHS = ....
        """         
        #TODO implement
        if len(left.typ.size) < len(ast.idx):
            raise TypeMismatchInExpression(ast)
        elif len(left.typ.size) == len(ast.idx):
            return VarZcode(left.typ.eleType)
        elif len(left.typ.size) > len(ast.idx):
            return VarZcode(ArrayType(left.typ.size[(len(left.typ.size) - len(ast.idx)):], left.typ.eleType))
        """
            # TODO kiểm tra TypeMismatchInExpression kiểm tra len(left.size) và len(ast.idx) 
            ^ len(left.size) < len(ast.idx) -> trả về lỗi TypeMismatchInExpression ví dụ
            number a[1,2]
            var c <- a[1,2,3]
            ^ len(left.size) = len(ast.idx) -> trả về type eleType không phải là arraytype
            number a[1,2]
            var c <- a[1,2] -> c : numbertype
            ^ len(left.size) > len(ast.idx) -> trả về arraytype cắt đi đoạn ban đầu
            number a[1,2,3]
            var c <- a[1] -> c : number c[2,3]                   
        """ 
        #TODO implement

    def visitArrayLiteral(self, ast, param):
        #* bước 1 chọn được type đã xác định kiểm trong ast.value (typ không phải là Zcode và ArrayZcode)
        typ = None
        for item in ast.value:
            checkTyp = self.visit(item, param)
            if (checkTyp.typ is not None) and (not (isinstance(checkTyp.typ, Zcode) or isinstance(checkTyp.typ, ArrayZcode))):
                typ = checkTyp.typ
                break
        
        #* Bước 2: xét kiểu từng phần tử
        #^ TH1 : typ is None nghĩa là trong array chỉ gồm Zcode và ArrayZcode nên return ArrayZcode
        if typ is None:
            #TODO implement
            return ArrayZcode(VarZcode())
        elif typ in [StringType(), BoolType(), NumberType()]:
            #^ TH2 : typ in [StringType, BoolType, NumberType] duyệt qua ast.value nếu typ từng phần tử có ArrayZcode hay là comparType bị khác thì nén TypeMismatchInExpression
            """_VD_
                [1, x, "2", [y]] -> lỗi TypeMismatchInExpression vì khác type trong array
                #* ta tìm được typ = NumberType (vì 1 là giá trị đầu tiên tìm được)
                #* ta bắt đầu so sánh LHS = NumberType, RHS = duyệt từ 0 -> n của từng phần tử trong ast.value
                    #! index = 0 -> LHS = NumberType, RHS = NubmerType -> đúng
                    #! index = 1 -> LHS = NumberType, RHS = VarZcode('x') -> x.typ = NumberType -> đúng
                    #! index = 2 -> LHS = NumberType, RHS = StringType -> sai -> TypeMismatchInExpression
                    #! index = 3 -> LHS = NumberType, RHS = ArrayZcode([VarZcode('y')]) -> sai -> TypeMismatchInExpression
            """
            for item in ast.value:
                RHS = self.visit(item, param)
                cmp = self.comparType(typ, RHS.typ)
                if cmp == "TMM":
                    raise TypeMismatchInExpression(ast)
                elif cmp == "infer":
                    RHS.typ = typ
            return VarZcode(ArrayType([len(ast.value)], typ))
        else:
            for item in ast.value:
                RHS = self.visit(item, param)
                print("Here is item of ast:", ast, typ.size, RHS.typ)
                cmp = self.comparType(typ, RHS.typ)
                print("cmp is", cmp)
                if cmp == "TMM":
                    raise TypeMismatchInExpression(ast)
                elif cmp == "infer":
                    pass
                elif cmp == "Right Type":
                    return VarZcode(ArrayType([len(ast.value)] + typ.size, typ))

            #^ TH3 : typ in arraytype duyệt qua ast.value giống TH2 nhưng nếu ArrayType yêu cầu dùng setTypeArray để chỉnh typ [[1,2]]
            """_VD_
                [x, [1], [1,2], [y]] -> lỗi TypeMismatchInExpression vì khác type trong array
                #* ta tìm được typ = ArrayType([1], numberType) (vì 1 là giá trị thứ 2 tìm được)
                #* ta bắt đầu so sánh LHS = ArrayType([1], numberType), RHS = duyệt từ 0 -> n của từng phần tử trong ast.value
                    #! index = 0 -> LHS = ArrayType([1], numberType), RHS = VarZcode('x') -> x.typ = ArrayType([1], numberType) -> đúng
                    #! index = 1 -> LHS = ArrayType([1], numberType), RHS = ArrayType([1], numberType) -> đúng
                    #! index = 2 -> LHS = ArrayType([1], numberType), RHS = ArrayType([2], numberType) -> sai -> TypeMismatchInExpression
                    #! index = 3 -> LHS = ArrayType([1], numberType), RHS = ArrayZcode([VarZcode('y')]) -> gọi setTypeArray
                        #* ta thu được y = numberType -> đúng
            """
            #TODO implement
            
            pass
    
    def visitBlock(self, ast, param):
        for item in ast.stmt:
            #! trường hợp gặp block
            if type(item) is Block: self.visit(item, [{}] + param)
            else:
                self.visit(item, param)
            
    def visitContinue(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        #! kiểm tra đang ở vòng for hay không
        if self.BlockFor == 0: raise MustInLoop(ast)   
    def visitNumberType(self, ast, param): return VarZcode(ast)
    def visitBoolType(self, ast, param): return VarZcode(ast)
    def visitStringType(self, ast, param): return VarZcode(ast)
    def visitArrayType(self, ast, param): return VarZcode(ast)
    def visitNumberLiteral(self, ast, param): return VarZcode(NumberType())
    def visitBooleanLiteral(self, ast, param): return VarZcode(BoolType())
    def visitStringLiteral(self, ast, param): return VarZcode(StringType())
