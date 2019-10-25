# import math
from math import sqrt
import numbers
import matrix as m

def zeroes(height, width):
       # """Creates a matrix of zeroes.
        #"""
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)
def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
class Matrix(object):
    # Constructor  
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid) # rows 
        self.w = len(grid[0]) # columns

    #0
    # Primary matrix math methods
    ############################
     
    def is_square(self):
        return self.h == self.w        
    #
    # Begin Operator Overloading
    ############################
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        # TODO - your code here
        #  for the matrix 1x1
        if self.h == 1 : 
            return self.g[0]
        # for Matrix 2x2
        elif self.h==2 :
            return ((self.g[0][0])*(self.g[1][1])-((self.g[1][0])*(self.g[0][1])))
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        else:
            su = 0
            for u in range(self.h):
                su += self.g[u][u]
            return su
  
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
            
        inverse_matrix=[]

        # TODO - your code here
        # Matrix 1x1
        if self.h == 1:
            inverse_matrix.append([1 / self[0][0]])
        # Matrix 2x2
        elif self.h == 2:
            
            # check the invertibility of the Matrix 
            if self[0][0] * self[1][1] == self[0][1] * self[1][0]:
                raise (ValueError,"The invertibility of this Matrix don't work ")
            else:
                e = self[0][0]                
                g = self[1][0]
                f = self[0][1]
                h = self[1][1]
                
                inverse_matrix = [[h, -f],[-g, e]]
                factor = 1 / (e * h - f * g)
   
                for i in range(len(inverse_matrix)):
                    for j in range(len(inverse_matrix[0])):
                        inverse_matrix[i][j] = factor * inverse_matrix[i][j]
    
        return Matrix(inverse_matrix)
    def T(self):                      
        """
        Returns a transposed copy of this Matrix.      
        """
        # TODO - your code 

        grid = zeroes(self.w, self.h)
        for p in range (self.h):
            for t in range(self.w):
                grid[t][p]=self.g[p][t]
        return grid
               
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s
    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
       # creation for the Matrix of Zeroes with self.h x self.w 
        grid_add = zeroes(self.h, self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                grid_add[i][j] = self.g[i][j] + other.g[i][j]
        return grid_add

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        # creation for the Matrix of Zeroes with self.h x self.w 
        grid_neg = zeroes(self.h, self.w)
     
        for j in range(self.h):
            for i in range(self.w):
                 grid_neg[j][i] = -1.0 *(self.g[j][i])
        return grid_neg  
    
    def __sub__(self, other):
        
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        # creation for the Matrix of Zeroes with self.h x other.w 
        grid_sub = zeroes(self.h, other.w)
        
        # traverse each element in matrix
        for o in range(self.h):
            for p in range(self.w):
                grid_sub[o][p] = self.g[o][p]-other.g[o][p]
                
        return grid_sub
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        # creation for the Matrix of Zeroes with self.h x other.w 
        grid_mul= zeroes(self.h, other.w)
        
        for x in range(self.h):
            for y in range(other.w):
                for z in range(other.h):
                    grid_mul[x][y] += self.g[x][z] * other.g[z][y]
        return grid_mul
    
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            
            grid_rmul = self
            for i in range(self.h):
                for j in range(self.w):
                    grid_rmul[i][j] *= other
            return grid_rmul