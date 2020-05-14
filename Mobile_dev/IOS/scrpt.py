import coremltools

coreml_model = coremltools.converters.keras.convert('yolo-tiny.h5', input_names='image', image_input_names='image',
                                                    input_name_shape_dict={'image': [None, 608, 608,
                                                                                     3]},  image_scale=1/255.)
coreml_model.input_description['image'] = 'Input image'

coreml_model.save('yolo-tiny.mlmodel')