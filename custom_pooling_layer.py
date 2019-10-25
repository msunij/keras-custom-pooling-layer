from keras.layers import Layer
#from matrix_factorization import matrix_factorization

class mf_pooling2D(Layer):

	def compute_output_shape(self,input_shape):
		#output_shape = (input_shape[0],input_shape[1]//2,input_shape[2]//,input_shape[3])
		shape = (2,2,1)
		return shape

	def call(self, inputs):
		print(type(inputs))
		return inputs