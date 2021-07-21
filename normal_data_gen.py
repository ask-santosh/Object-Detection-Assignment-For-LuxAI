# Importing necessary library
import Augmentor

# Passing the path of the image directory
p = Augmentor.Pipeline("./TrainYourOwnYOLO-master/Data/Source_Images/Training_Images")

# Defining augmentation parameters and generating 5 samples
p.flip_left_right(0.5)
# p.black_and_white(0.1)
p.rotate(0.3, 10, 10)
p.skew(0.4, 0.5)
p.resize(probability=1.0, width=320, height=320)
p.zoom(probability=0.2, min_factor=1.1, max_factor=1.5)
p.sample(200)
