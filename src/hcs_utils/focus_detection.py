import numpy as np
from scipy.ndimage import gaussian_filter

def adaptive_focus(plane_images_stack, expected_object_size=30):
    sigma = expected_object_size*7/6

    h, w, num_of_planes = plane_images_stack.shape
    convolved_map = np.zeros(plane_images_stack.shape)

    for i in range(num_of_planes):
        im = (plane_images_stack[:,:,i])
        dx, dy = np.gradient(im)
        gradient_mag = np.power(dx,2)+np.power(dy,2)
        convolved_map[:,:,i] = gaussian_filter(gradient_mag, sigma=sigma)
        
    depth_map = np.argmax(convolved_map, axis=2)
    focused_composite_image = np.zeros((h,w))
    for i in range(h):
        for j in range(w):
            focused_composite_image[i,j] = plane_images_stack[i,j,depth_map[i,j]]

    return focused_composite_image


def select_focus_plane(plane_images_stack):
    h, w, num_of_planes = plane_images_stack.shape

    tg = np.array((num_of_planes,))

    for i in range(num_of_planes):
        im = (plane_images_stack[:,:,i])
        dx, dy = np.gradient(im)
        tg[i] = np.sum(np.power(dx,2))+np.sum(np.power(dy,2))

    best_plane_id = np.argmax(tg)

    return plane_images_stack[:,:,best_plane_id]
