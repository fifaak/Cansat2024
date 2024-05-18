import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.preprocessing.image import load_img, img_to_array

def GET_PIXEL(image_path, model_path, threshold_):
    # Dummy dice_coefficient function, replace it with your actual implementation
    def dice_coefficient(y_true, y_pred):
        smooth = 1e-6
        y_true_f = np.ravel(y_true)
        y_pred_f = np.ravel(y_pred)
        intersection = np.sum(y_true_f * y_pred_f)
        return (2. * intersection + smooth) / (np.sum(y_true_f) + np.sum(y_pred_f) + smooth)

    # Define custom loss function
    def dice_loss(y_true, y_pred):
        return 1 - dice_coefficient(y_true, y_pred)

    # Load the U-Net model with custom objects (including custom loss function)
    with keras.utils.custom_object_scope({'dice_loss': dice_loss, 'dice_coefficient': dice_coefficient}):
        # Define custom IoU metric function
        def iou_metric(y_true, y_pred):
            intersection = np.logical_and(y_true, y_pred)
            union = np.logical_or(y_true, y_pred)
            iou = np.sum(intersection) / np.sum(union)
            return iou

        # Load the U-Net model with custom objects (including custom loss function and metric)
        model = keras.models.load_model(model_path, compile=False)
        model.compile(optimizer='adam', loss=dice_loss, metrics=[iou_metric])

    # Function to preprocess an image for segmentation
    def preprocess_for_segmentation(image_path, target_size=(256, 256)):
        img = load_img(image_path, target_size=target_size)
        img_array = img_to_array(img) / 255.0  # Normalize pixel values to [0, 1]
        return np.expand_dims(img_array, axis=0)

    # Function to perform segmentation using the U-Net model
    def segment_image(model, image_path):
        preprocessed_image = preprocess_for_segmentation(image_path)
        segmentation_mask = model.predict(preprocessed_image)[0, :, :, 0]
        return segmentation_mask

    # Perform segmentation
    segmentation_result = segment_image(model, image_path)
    threshold = threshold_

    # Apply threshold to the segmentation mask
    binary_mask = (segmentation_result > threshold).astype(np.uint8)
    oil_spill_area_pixel = np.sum(binary_mask)
    
    return oil_spill_area_pixel
