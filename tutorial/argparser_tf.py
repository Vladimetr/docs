import tensorflow as tf

# ------------ run: python3 argparser_tf.py -model some_name 
# ------------ output: okey some_name 

flags = tf.app.flags
FLAGS = tf.flags.FLAGS

def create_flags():
    # -model, default_value, dicription for help
    tf.flags.DEFINE_string('model', None, 'model name')
    

def main():
    create_flags()
    print('okey', FLAGS.model) 
    

if __name__ == '__main__':   
    main()    
