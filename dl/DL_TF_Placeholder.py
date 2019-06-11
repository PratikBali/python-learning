import tensorflow as tf

# Build Computational graph
node1 = tf.compat.v1.placeholder(tf.float32)
node2 = tf.compat.v1.placeholder(tf.float32)

output = node1 + node2

# Run computational graph
sobj = tf.compat.v1.Session()

print(sobj.run(
    output, {
        node1: [1, 3],
        node2: [4, 5],
    }))

sobj.close()
