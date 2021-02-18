from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Finish the new Observer class!
class Observer():
    '''
    This class creates an artificial night sky observer.
    '''
    __slots = ['im1_filename', 'im2_filename', 'im1_data', 'im2_data']
    # This function will get called automatically
    # when a new "observer" is created
    def __init__(self,im1_filename,im2_filename):
        '''
        When initializing the observer, the "red" image should be given
        as the first input argument and the "ir" image should be the second input
        '''
        self.im1_filename = im1_filename
        self.im2_filename = im2_filename
        self.load_images(im1_filename,im2_filename)
        
    def load_images(self, im1_filename, im2_filename):
        '''
        This function takes two filepaths as arguments and loads the corresponding fits files as attributes for the class
        '''
        self.im1_data = fits.open(im1_filename)[0].data
        self.im2_data = fits.open(im2_filename)[0].data
    
    def make_composite(self):
        '''
        This function is incomplete! Make sure to finish it and
        then update this docstring to explain what the function does!
        '''
        # Define the array for storing RGB values
        rgb = np.zeros((self.im1_data.shape[0],self.im1_data.shape[1],3))
        
        # Define a normalization factor for our denominator using the R filter image
        norm_factor = self.im1_data.astype("float").max()
        
        # Compute the red channel values and then clip them to ensure nothing is > 1.0
        rgb[:,:,0] = 1.5 * (self.im2_data.astype("float")/norm_factor)
        rgb[:,:,0][rgb[:,:,0] > 1.0] = 1.0
        
        #compute green channel values
        rgb[:, :, 1] = ((self.im2_data.astype("float") + self.im1_data.astype("float"))/2)/norm_factor
        rgb[:,:,1][rgb[:,:,1] > 1.0] = 1.0
    
        #compute blue channel values
        rgb[:, :, 2] = self.im1_data.astype("float")/norm_factor
        rgb[:,:,2][rgb[:,:,2] > 1.0] = 1.0
        
        plt.imshow(rgb, origin='lower')
        
    def calc_stats(self):
        print('image_data_1: Mean: ', self.im1_data.mean(), ' Stddev: ', self.im1_data.std(), ' Max: ', self.im1_data.max(), ' Min: ', self.im1_data.min())
        print('image_data_2: Mean: ', self.im2_data.mean(), ' Stddev: ', self.im2_data.std(), ' Max: ', self.im2_data.max(), ' Min: ', self.im2_data.min())
