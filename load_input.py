import numpy as np
import matplotlib as mpl
import create_data_natural

mpl.use('Agg')
import matplotlib.pyplot as plt


class InputData(object):
    """An object of InputData must have images and labels.

    Attributes:
        images: A list of lists of image pixels.
        labels: A list of one-hot label lists.
    """

    def __init__(self, folder="", images=[], labels=[]):
        """Return an InputData object."""
        self.folder = folder
        self.images = []
        self.labels = []
        self.length = 0


    def get_train(self, even=None, min_blobs=1, max_blobs=1): # MT
        """Generate and get train images and labels."""
        self.images, self.labels = create_data_natural.generate_data(even, min_blobs, max_blobs)
        self.length = len(self.images)
        
        
    def get_density(self, even=None, min_blobs=1, max_blobs=1): # MT
        """Generate and get train images and labels."""
        self.images, self.labels = create_data_natural.generate_data(even, min_blobs, max_blobs, density=True)
        self.length = len(self.images)


    def get_test(self, even=None, min_blobs=1, max_blobs=1): # MT
        """Generate and get test images and labels."""
        self.images, self.labels = create_data_natural.generate_data(even, min_blobs, max_blobs) # MT
        self.length = len(self.images)


    def load_sample(self):
        """Load the sample set and labels."""
        self.load_images(self.folder + "/sampleSet.txt")
        self.load_labels(self.folder + "/sampleLabel.txt")


    def load_train(self):
        """Load the train set and labels."""
        self.load_images(self.folder + "/trainSet.txt")
        self.load_labels(self.folder + "/trainLabel.txt")


    def load_test(self):
        """Load the test set and labels."""
        self.load_images(self.folder + "/testSet.txt")
        self.load_labels(self.folder + "/testLabel.txt")


    def load_images(self, filename):
        """Load the image data"""
        self.images = self.load(filename)
        self.length = len(self.images)


    def load_labels(self, filename):
        """Load the image data"""
        self.labels = self.load(filename)


    def load(self, filename):
        """Load the data from text file."""
        file = open(filename, "r")
        text = file.read()
        file.close()
        text = text.replace(']', '],').replace('],]', ']]').replace(']],', ']]')
        text = text.replace('.', ',').replace(',]', ']')
        aList = eval(text)
        return aList


    def get_length(self):
        """Return the number of images."""
        return self.length


    def next_batch(self, batch_size):
        """Returns a batch of size batch_size of data."""
        all_idx = np.arange(0, self.length)
        np.random.shuffle(all_idx)
        batch_idx = all_idx[:batch_size]
        batch_imgs = [self.images[i] for i in batch_idx]
        batch_lbls = [self.labels[i] for i in batch_idx]
        return batch_imgs, batch_lbls

    def next_batch_nds(self, batch_size):
        """Returns a batch of size batch_size of data."""
        all_idx = np.arange(0, self.length)
        batch_idx = all_idx[:batch_size]
        batch_imgs = [self.images[i] for i in batch_idx]
        batch_lbls = [self.labels[i] for i in batch_idx]
        return batch_imgs, batch_lbls

    def split_data(self):
        """Returns the first half and latter half data of each number."""
        all_idx = np.arange(0, 9000)# self.length)
        nOfImgs = 1000
        fh_idx = all_idx[0:nOfImgs//2] # first half index
        lh_idx = all_idx[nOfImgs//2:nOfImgs] # latter half index
        for i in range(1,9):
            fh_idx = np.append(fh_idx, all_idx[nOfImgs*i:nOfImgs*i+nOfImgs//2])
            lh_idx = np.append(lh_idx, all_idx[nOfImgs*i+nOfImgs//2:nOfImgs*(i+1)])
        fh_imgs = [self.images[i] for i in fh_idx]
        fh_lbls = [self.labels[i] for i in fh_idx]
        lh_imgs = [self.images[i] for i in lh_idx]
        lh_lbls = [self.labels[i] for i in fh_idx]
        return fh_imgs, fh_lbls, lh_imgs, lh_lbls

    def print_img_at_idx(self, idx):
        """Prints the image at index idx."""
        img = self.images[idx]
        print_img(img)


    def get_label(self, idx):
        """Returns the label."""
        return self.labels[idx]


def test_this():
    """Test out this class."""
    myData = InputData()
    myData.load_sample()
    print(myData.get_length())
    x_train, y_train = myData.next_batch(10)
    for i, img in enumerate(x_train):
        print_img(img)
        print(y_train[i])


def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


def print_img(img):
    """Prints the image."""
    matrix = list(chunks(img, 100))
    plt.imshow(matrix, interpolation="nearest", origin="upper")
    plt.colorbar()
    plt.show()

