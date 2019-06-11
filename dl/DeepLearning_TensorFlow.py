import tensorflow as tf

# build computation graph
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0, tf.float32)

# print(node1,node2)

# run computational graph
sobj = tf.compat.v1.Session()
print(sobj.run([node1, node2]))

sobj.close()
