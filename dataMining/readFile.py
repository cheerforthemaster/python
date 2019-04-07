import scipy.io
from dataMining import *

data = scipy.io.loadmat('BU3D_feature.mat')
dataMatrix=data.get('data')
orignalMat=dataMatrix
dataMatrix=np.delete(dataMatrix,-1,axis=1)
print(dataMatrix)
#dataMatrix=dataMatrix.T
lowDDataMat, reconMat = pca(dataMatrix,11)
fig(lowDDataMat,orignalMat)