from tensorflow.keras.optimizers import legacy
from tensorflow.keras.models import model_from_json

def load_model(h5_path , json_path):

    with open(json_path) as json_file:
        loaded_model_json = json_file.read()

    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights(h5_path)
    
    # evaluate loaded model on test data
    optimizer = legacy.Adam(learning_rate=0.001, beta_1=0.869, beta_2=0.995)

    loaded_model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics= ['accuracy'])

    return loaded_model


