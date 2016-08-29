#coding:utf-8
#k-近邻算法
# 原理：样本集中每个数据都存在标签，输入没有标签的新数据，
# 将新数据的每个特征与样本集中数据对应的特征进行比较，
# 然后算法提取样本集中特征最相似数据（最近邻）的分类标签。
# 选择K个最相似数据，将出现次数最多的分类标签，作为新数据的标签


from numpy import *  #导入科学计算包
import operator      #导入运算符模块



# 第一步：收集数据，准备数据，得到可以计算的结构化数据
#创建数据集和标签
class func:
    def createDataSet(self):
        group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
        labels = ['A','A','B','B']
        print group
        print labels
        return group,labels

    def classify0(self,intX,dataSet,labels,k):
        dataSetSize = dataSet.shape[0]#shapes返回列表【行数，列数】，取第一维，就是行数
        diffMat = tile(intX,(dataSetSize,1))-dataSet#tile函数用来复制数组，要和n个训练集求距离，需要复制n份
        sqDiffMat = diffMat**2
        sqDistances = sqDiffMat.sum(axis=1)
        distances = sqDistances**0.5
        sortedDistIndicies = distances.argsort()#argsort给出排序后的下标索引
        classCount = {}
		
		#以下代码，通过下标，使标签矩阵与数据矩阵产生联系一一对应
        for i in range (k):
            voteIlabel = labels[sortedDistIndicies[i]]#距离最近的几个训练集的标签
            classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1#得到前K个训练集中，到每一类标签的次数之和
        sortClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=(True))
        return sortClassCount[0][0]

if __name__=='__main__':
    print "begin...."
    kNN = func()
    group,labels = kNN.createDataSet()
    print group
    print labels
    result = kNN.classify0([0,0],group,labels,3)#运行，测试【0,0】的标签是什么
    print result

