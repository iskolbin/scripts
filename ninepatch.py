#!/usr/bin/env python



import PIL.Image
import sys
from PIL.Image import ANTIALIAS
    
def main():
    print'Ninepatch by iskolbin'
    
    if len( sys.argv ) != 9:
        print 'Scales image by ninepatch method'
        print 'Usage: ninepatch.py <input file> <output file> <x1> <x2> <y1> <y2> <output width> <output height>' 
        print 'Example: ninepatch.py button.png button_scl.png 10 50 10 50 200 200'
        print 'where x1, x2, y1, y2:'
        print ''
        print '####x1####x2#####'
        print '#####|#####|#####'
        print 'y1---+-----+-----'
        print '#####|#####|#####'
        print '#####|#####|#####'
        print 'y2---+-----+-----'
        print '#####|#####|#####'
        print '#####|#####|#####'
    else:
        _,infile, outfile, x1, x2, y1, y2, w, h = sys.argv
        x1, x2, y1, y2, w, h = int( x1 ), int( x2 ), int( y1 ), int( y2 ), int( w ), int( h )
        
        im = PIL.Image.open( infile )
        imw, imh = im.size
        im_nw, im_n, im_ne = im.crop((0,0,x1,y1)), im.crop((x1,0,x2,y1)), im.crop((x2,0,imw,y1))
        im_w,  im_c, im_e  = im.crop((0,y1,x1,y2)), im.crop((x1,y1,x2,y2)), im.crop((x2,y1,imw,y2))
        im_sw, im_s, im_se = im.crop((0,y2,x1,imh)), im.crop((x1,y2,x2,imh)), im.crop((x2,y2,imw,imh))
        
        w1_0,h1_0 = im_nw.size
        w2_0,_ = im_n.size
        w3_0,_ = im_ne.size
        _,h2_0 = im_w.size
        _,h3_0 = im_sw.size
        
        w1, w2, w3 = w1_0, w-w1_0-w3_0, w3_0
        h1, h2, h3 = h1_0, h-h1_0-h3_0, h3_0
        
        x1, x2, x3 = 0, x1, x1+w2
        y1, y2, y3 = 0, y1, y1+h2
        
        om = PIL.Image.new( im.mode, (w,h) )
        om.paste( im_nw, (x1,y1))
        om.paste( im_n.resize((w2,h1_0), ANTIALIAS), (x2,y1))
        om.paste( im_ne, (x3,y1))
        om.paste( im_w.resize((w1_0,h2), ANTIALIAS), (x1,y2))
        om.paste( im_c.resize((w2,h2)), (x2,y2))
        om.paste( im_e.resize((w3_0,h2), ANTIALIAS), (x3,y2))
        om.paste( im_sw, (x1,y3))
        om.paste( im_s.resize((w2,h3_0), ANTIALIAS), (x2,y3))
        om.paste( im_se, (x3,y3))
        
        om.save( outfile )
        print 'succesfully written to %s' % outfile

if __name__ == "__main__":
    main()
