import tensorflow as tf

# Build computational graph
node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0, tf.float32)

output = node1 * node2

# Run computational graph
sobj = tf.compat.v1.Session()
print(sobj.run(output))

sobj.close()
