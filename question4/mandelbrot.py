import numpy as np
import matplotlib.pyplot as plt

X_DIM = 500
Y_DIM = 500

def main():
    show_mandelbrot_set_img()

def mandelbrot_set(c, seed=0, max_iter=500):
    z = seed

    for i in xrange(max_iter):
        if abs(z) > 2: # number does not belong to set
            return i
        z = z**2 + c

    return 0

def show_mandelbrot_set_img():
    x_pixels = np.linspace(-1.9999, 2, X_DIM, endpoint=False, dtype=np.complex_)
    y_pixels = np.linspace(-1.9999j, 2j, Y_DIM, endpoint=False)

    #print y_pixels.shape

    grid = np.tile(np.array([x_pixels]).transpose(), (1, Y_DIM))

    grid += y_pixels
    
    mandelbrot_vec = np.vectorize(mandelbrot_set)
    grid = mandelbrot_vec(grid)
    #print grid.shape
    print grid[0]

    plt.figure()
    plt.imshow(grid)
    plt.show()
    
if __name__ == "__main__":
    main()
