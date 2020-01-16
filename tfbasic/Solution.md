问题解决：  
1、Session  
with tf.compact.v1.Session() as sess:  //session必需有（）  

第2个要调用tf.compat.v1.disable_eager_execution()，才能使用1.x的语法。  
本手册基于 TensorFlow 的 Eager Execution 模式。  
在 TensorFlow 1.X 版本中， 必须 在导入 TensorFlow 库后调用 tf.enable_eager_execution() 函数以启用 Eager Execution 模式。  
在 TensorFlow 2.0 版本中，Eager Execution 模式将成为默认模式，  
无需额外调用 tf.enable_eager_execution() 函数（不过若要关闭 Eager Execution，则需调用 tf.compat.v1.disable_eager_execution() 函数）。