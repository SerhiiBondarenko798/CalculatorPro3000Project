class CFunctions:
	def __init__(self,**kwargs):
		super(CFunctions, self).__init__(**kwargs)
		self.result = 0
		self.operation = '0'
	def CalculatePls(self):
		func = self.operation
		form_st = Stack()
		length = len(func)
		result = ''
		
		for i in range(length):
			#for numbers
			if (self.__isNumber(func[i]) or (func[i] == '-' and i == 0)  or (i > 0 and func[i-1] == '(' and func[i] == '-')):
				if ((i+1)==length or self.__isOperator(func[i+1])  or func[i+1] == '(' or func[i+1] == ')' ):
					result = result + func[i] + ' '
				else:
					result = result + func[i]
			#brackets

			elif (func[i]=='('):
				form_st.push('(')


			elif (func[i]==')'):
				while (form_st.top() != ('(')):
					result = result + form_st.pop() + ' '
				form_st.pop()

			#operations

			elif (self.__isOperator(func[i])):
				while (not(form_st.isEmpty()) and (self.__OpPriority(form_st.top()) >= self.__OpPriority(func[i]))):
					result = result + form_st.pop() + ' '
				form_st.push(func[i])

			#else

			else:
				print('kakayato dich')


		if (form_st.size()>0):
			for i in range(form_st.size() - 1):
				result= result + form_st.pop() + ' '
			result= result + form_st.pop()
		return result

	def __isNumber(self,chvar):
		return((('0'<= chvar) and (chvar <= '9')) or (chvar == '.'))

	def __isOperator(self,chvar):
		check_list = ['+','-','*','/','^']
		return (chvar in check_list)

	def __OpPriority(self,chvar):
		Priority_list = {
		'+': 1,
		'-': 1,
		'*': 2,
		'/': 2,
		'^': 3}
		try:
			res = Priority_list [chvar]
		except KeyError as e:
			res = 0
		return res


	"""C_Operations"""
	def __Addition(x,y):
		return (float(x) + float(y))
	def __Subtraction(x,y):
		return (float(x) - float(y))
	def __Multiplication(x,y):
		return (float(x) * float(y))
	def __Division(x,y):
		return (float(x) / float(y))
	def __Exponentiation(x,y):
		return (float(x) ** float(y))


class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def top(self):
		return self.items[-1]

	def base(self):
		return self.items[0]



ps=CFunctions()
ps.operation = '4+1-3*(5+6.7)'
izi =ps.CalculatePls()
print(izi)				
