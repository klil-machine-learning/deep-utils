from keras.preprocessing import image

def get_data(path, target_size=(244, 244)):
    batches = image.ImageDataGenerator().flow_from_directory(path, shuffle = False, batch_size = 1, class_mode = None, target_size = target_size)
    return np.concatenate([batches.next() for i in range(batches.samples)])
