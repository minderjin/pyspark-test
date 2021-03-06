from pyspark import SparkContext

logFile = "/home/spark/spark/README.md"     # Should be some file on your system
sc = SparkContext("local", "Simple App")
logData = sc.textFile(logFile).cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print("###################################################")
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

sc.stop()
