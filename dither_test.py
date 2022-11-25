from dither import Dither

DEBUGMODE = False
default_method = 'bayer4x4'
default_palette = 'cga_mode4_2_high'


if __name__ == '__main__':
    dither = Dither()
    pilim = dither.open_image('images/parrot.jpg')
    matrix = dither.pil2numpy(pilim)
    # dith = dither.ordered_dither(matrix, '1bit_gray', 'bayer4x4')
    dith = dither.error_diffusion(matrix, '1bit_gray', 'jajuni')
    out = dither.numpy2pil(dith)
    out.show()

    # image = utils.open_image('images/parrot.jpg')
    # image_matrix = utils.pil2numpy(image)
    #
    # dither_matrix = ordered_dithering._ordered_dither(image_matrix, '1bit_gray', ordered_dithering._diffusion_matrices['bayer4x4'])
    # dither_image = utils.numpy2pil(dither_matrix)
    #
    # dither_image.show()
    # #     dither_image.save(args.output)
