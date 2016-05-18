import tensorflow as tf


def compute_accuracy(network, xs, ys):
    correct_prediction = tf.equal(tf.argmax(network.layers_output.iloc[-1], 1),
                                  tf.argmax(network.target_placeholder, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    return network.sess.run(accuracy, feed_dict={network.data_placeholder: xs,
                                                 network.target_placeholder: ys})