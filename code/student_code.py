import numpy as np

def my_imfilter(image, filter):
  """
  Apply a filter to an image. Return the filtered image.

  Args
  - image: numpy nd-array of dim (m, n, c)
  - filter: numpy nd-array of dim (k, k)
  Returns
  - filtered_image: numpy nd-array of dim (m, n, c)

  HINTS:
  - You may not use any libraries that do the work for you. Using numpy to work
   with matrices is fine and encouraged. Using opencv or similar to do the
   filtering for you is not allowed.
  - I encourage you to try implementing this naively first, just be aware that
   it may take an absurdly long time to run. You will need to get a function
   that takes a reasonable amount of time to run so that the TAs can verify
   your code works.
  - Remember these are RGB images, accounting for the final image dimension.
  """

  assert filter.shape[0] % 2 == 1
  assert filter.shape[1] % 2 == 1

  ############################
  ### TODO: YOUR CODE HERE ###

  #raise NotImplementedError('`my_imfilter` function in `student_code.py` ' +
  #  'needs to be implemented')

  # Pad the input image with mirrored edges
  pad_h = int((filter.shape[0]-1)/2)
  pad_w = int((filter.shape[1]-1)/2)
  padded_image = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w), (0, 0)), 'symmetric')

  # Apply the filter to the input image
  filtered_image = image.copy()
  for layer in range(image.shape[2]):
      for row in range(image.shape[0]):
          for col in range(image.shape[1]):
              filtered_image[row][col][layer] = np.sum(np.multiply(padded_image[row:row + filter.shape[0], col:col + filter.shape[1], layer], filter))

  ### END OF STUDENT CODE ####
  ############################

  return filtered_image

def create_hybrid_image(image1, image2, filter):
  """
  Takes two images and creates a hybrid image. Returns the low
  frequency content of image1, the high frequency content of
  image 2, and the hybrid image.

  Args
  - image1: numpy nd-array of dim (m, n, c)
  - image2: numpy nd-array of dim (m, n, c)
  Returns
  - low_frequencies: numpy nd-array of dim (m, n, c)
  - high_frequencies: numpy nd-array of dim (m, n, c)
  - hybrid_image: numpy nd-array of dim (m, n, c)

  HINTS:
  - You will use your my_imfilter function in this function.
  - You can get just the high frequency content of an image by removing its low
    frequency content. Think about how to do this in mathematical terms.
  - Don't forget to make sure the pixel values are >= 0 and <= 1. This is known
    as 'clipping'.
  - If you want to use images with different dimensions, you should resize them
    in the notebook code.
  """

  assert image1.shape[0] == image2.shape[0]
  assert image1.shape[1] == image2.shape[1]
  assert image1.shape[2] == image2.shape[2]

  ############################
  ### TODO: YOUR CODE HERE ###

  #raise NotImplementedError('`create_hybrid_image` function in ' + 
  #  '`student_code.py` needs to be implemented')

  # Apply filter to obtain low_frequency image1
  low_frequencies = my_imfilter(image1, filter)

  # Apply filter to obtain low_frequency image2
  low_freq_image2 = my_imfilter(image2, filter)

  # Subtract low_frequency image2 from original image to obtain high_frequencies image2
  high_frequencies = image2 - low_freq_image2
  
  # Sum  low_frequencies & high_frequencies to obtain hybrid image
  hybrid_image = low_frequencies + high_frequencies
 
  ### END OF STUDENT CODE ####
  ############################

  return low_frequencies, high_frequencies, hybrid_image
