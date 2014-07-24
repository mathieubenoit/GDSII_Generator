#!/usr/bin/python
import os
import numpy
import gdspy

print('Using gdspy module version ' + gdspy.__version__)

def GenerateSquarePixel(pitchX,pitchY,ALinner_width,ALouter_width,IMPinner_width,IMPouter_width,niinner_width,niouter_width,PORadius,contact_radius,UBM_radius,cellname='PIXEL'):
    
    pixel_cell = gdspy.Cell(cellname)

    ## Aluminium Layer
    center = (0,0)
    #ALinner_width = 15
    #ALouter_width = 20
    hiw= ALinner_width/2.0
    radius = (ALouter_width - ALinner_width) / 2.0

    ##### Body
    pixel_cell.add(gdspy.Rectangle(6,(-ALinner_width/2.0+center[0],-ALinner_width/2.0+center[1]), (ALinner_width/2.0+center[0], ALinner_width/2.0+center[1])))
    ##### Sides
    pixel_cell.add(gdspy.Rectangle(6,(hiw,-hiw),(hiw+radius,hiw)))
    pixel_cell.add(gdspy.Rectangle(6,(-hiw,-hiw),(hiw,-hiw - radius)))
    pixel_cell.add(gdspy.Rectangle(6,(-hiw,hiw),(-hiw-radius,-hiw)))
    pixel_cell.add(gdspy.Rectangle(6,(hiw,hiw),(-hiw,hiw+radius)))

    ##### Rounded corners
    pixel_cell.add(gdspy.Round(6, (-hiw, -hiw), radius, inner_radius=0,
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi / 2.0))
    pixel_cell.add(gdspy.Round(6, (hiw,-hiw), radius, inner_radius=0,
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
    pixel_cell.add(gdspy.Round(6, (hiw, hiw), radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
    pixel_cell.add(gdspy.Round(6, (-hiw, hiw), radius, inner_radius=0,
                          initial_angle=numpy.pi/2.0,
                          final_angle=numpy.pi))

    ## Nitride Layer
    center = (0,0)
    hiw= niinner_width/2.0
    radius = (niouter_width - niinner_width) / 2.0

    ##### Body
    pixel_cell.add(gdspy.Rectangle(3,(-niinner_width/2.0+center[0],-niinner_width/2.0+center[1]), (niinner_width/2.0+center[0], niinner_width/2.0+center[1])))
    ##### Sides
    pixel_cell.add(gdspy.Rectangle(3,(hiw,-hiw),(hiw+radius,hiw)))
    pixel_cell.add(gdspy.Rectangle(3,(-hiw,-hiw),(hiw,-hiw - radius)))
    pixel_cell.add(gdspy.Rectangle(3,(-hiw,hiw),(-hiw-radius,-hiw)))
    pixel_cell.add(gdspy.Rectangle(3,(hiw,hiw),(-hiw,hiw+radius)))

    ##### Rounded corners
    pixel_cell.add(gdspy.Round(3, (-hiw, -hiw), radius, inner_radius=0,
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi / 2.0))
    pixel_cell.add(gdspy.Round(3, (hiw,-hiw), radius, inner_radius=0,
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
    pixel_cell.add(gdspy.Round(3, (hiw, hiw), radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
    pixel_cell.add(gdspy.Round(3, (-hiw, hiw), radius, inner_radius=0,
                          initial_angle=numpy.pi/2.0,
                          final_angle=numpy.pi))


    ## Implant Layer
    center = (0,0)
    #IMPinner_width = 12
    #IMPouter_width = 15
    hiw= IMPinner_width/2.0
    radius = (IMPouter_width - IMPinner_width) / 2.0

    ##### Body
    pixel_cell.add(gdspy.Rectangle(8,(-IMPinner_width/2.0+center[0],-IMPinner_width/2.0+center[1]), (IMPinner_width/2.0+center[0], IMPinner_width/2.0+center[1])))
    ##### Sides
    pixel_cell.add(gdspy.Rectangle(8,(hiw,-hiw),(hiw+radius,hiw)))
    pixel_cell.add(gdspy.Rectangle(8,(-hiw,-hiw),(hiw,-hiw - radius)))
    pixel_cell.add(gdspy.Rectangle(8,(-hiw,hiw),(-hiw-radius,-hiw)))
    pixel_cell.add(gdspy.Rectangle(8,(hiw,hiw),(-hiw,hiw+radius)))

    ##### Rounded corners
    pixel_cell.add(gdspy.Round(8, (-hiw, -hiw), radius, inner_radius=0,
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi / 2.0))
    pixel_cell.add(gdspy.Round(8, (hiw,-hiw), radius, inner_radius=0,
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
    pixel_cell.add(gdspy.Round(8, (hiw, hiw), radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
    pixel_cell.add(gdspy.Round(8, (-hiw, hiw), radius, inner_radius=0,
                          initial_angle=numpy.pi/2.0,
                          final_angle=numpy.pi))

    # Contact Layer

    #pixel_cell.add(gdspy.Round(2, (3*pitchX/16., 3*pitchY/16.), 2.5))
    #pixel_cell.add(gdspy.Round(2, (-3*pitchX/16., -3*pitchY/16.), 2.5))
    #pixel_cell.add(gdspy.Round(2, (-3*pitchX/16., 3*pitchY/16.), 2.5))
    #pixel_cell.add(gdspy.Round(2, (3*pitchX/16.,-3*pitchY/16.), 2.5))
    pixel_cell.add(gdspy.Round(5,(0,0),contact_radius))


    # UBM Layer
    pixel_cell.add(gdspy.Round(9, (0,0), UBM_radius))    

    # Passivation Opening
    pixel_cell.add(gdspy.Round(15, (0,0), PORadius))


def GenerateRoundPixel(pitchX,pitchY,metal_radius,implant_radius,contact_radius,po_radius,cellname='PIXEL'):
    pixel_cell = gdspy.Cell(cellname)

    ## Aluminium Layer
    center = (0,0)
    pixel_cell.add(gdspy.Round(6, center, metal_radius))

    ## Implant Layer
    pixel_cell.add(gdspy.Round(8, center, implant_radius))

    ## Passivation Opening Layer
    pixel_cell.add(gdspy.Round(15, center, po_radius))

    ## Contact Opening
    pixel_cell.add(gdspy.Round(5, center, contact_radius))


def GeneratePixelArray(pixelcellname='PIXEL',edgecell='EDGE',nX=256,nY=256,pitchX=55,pitchY=55,topcellname='TOP') : 
    mpx_cell = gdspy.Cell(topcellname)
    mpx_cell.add(gdspy.CellArray(pixelcellname, nX, nY,(pitchX,pitchY),(pitchX/2.,pitchY/2.)))
    mpx_cell.add(gdspy.CellArray(edgecell, 1, 1,(0,0),(nX*pitchX/2.,nY*pitchY/2.)))
    mpx_cell.add(gdspy.CellArray('GR', 1, 1,(0,0),(nX*pitchX/2.,nY*pitchY/2.)))



def GenerateEdge(pitchX,pitchY,nX,nY,pixel_to_edge_dist,trench_width,cellname='EDGE') :

    gr_cell = gdspy.Cell(cellname)

    print nX,nY,pitchX,pitchY
    
    xmin=-1*(nX/2.)*pitchX - pixel_to_edge_dist - trench_width
    ymin=-1*(nY/2.)*pitchY - pixel_to_edge_dist - trench_width
    xmax=-1*(nX/2.)*pitchX - pixel_to_edge_dist
    ymax=(nY/2.)*pitchY + pixel_to_edge_dist + trench_width
    print xmin,xmax,ymin, ymax
    gr_cell.add(gdspy.Rectangle(2,(xmin,ymin),(xmax,ymax)))

    xmin=(nX/2.)*pitchX + pixel_to_edge_dist 
    ymin=-1*(nY/2.)*pitchY - pixel_to_edge_dist - trench_width
    xmax=(nX/2.)*pitchX + pixel_to_edge_dist + trench_width
    ymax=(nY/2.)*pitchY + pixel_to_edge_dist + trench_width
    print xmin,xmax,ymin,ymax
    gr_cell.add(gdspy.Rectangle(2,(xmin,ymin),(xmax,ymax)))

    xmin=-1*(nX/2.)*pitchX - pixel_to_edge_dist 
    ymin=-1*(nY/2.)*pitchY - pixel_to_edge_dist - trench_width
    xmax=(nX/2.)*pitchX + pixel_to_edge_dist
    ymax=-1*(nY/2.)*pitchY - pixel_to_edge_dist
    print xmin,xmax,ymin,ymax
    gr_cell.add(gdspy.Rectangle(2,(xmin,ymin),(xmax,ymax)))

    xmin=-1*(nX/2.)*pitchX - pixel_to_edge_dist
    ymin=(nY/2.)*pitchY + pixel_to_edge_dist 
    xmax=(nX/2.)*pitchX + pixel_to_edge_dist
    ymax=(nY/2.)*pitchY + pixel_to_edge_dist + trench_width
    print xmin,xmax,ymin,ymax
    gr_cell.add(gdspy.Rectangle(2,(xmin,ymin),(xmax,ymax)))

def GenerateGuardRings(inner_size_X,inner_size_Y, positions, inner_edge, outer_edge, doping_width, cellname='GR',bump_radius=10.) :
        gr_cell = gdspy.Cell(cellname)
        for i,position in enumerate(positions) :
            print "building GR %i position : %f"%(i,position)
            ## Aluminium Layer
            center = (0,0)
            ALinner_width = 15
            ALouter_width = 20
            hiw= ALinner_width/2.0
            radius = position+outer_edge[i]
            ##### Sides
            gr_cell.add(gdspy.Rectangle(6,(inner_size_X/2.+position-inner_edge[i],-inner_size_X/2.),(inner_size_X/2.+position+outer_edge[i],inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(6,(inner_size_X/2.,inner_size_X/2.+position - inner_edge[i]),(-inner_size_X/2.,inner_size_X/2.+position+outer_edge[i])))
            gr_cell.add(gdspy.Rectangle(6,(-inner_size_X/2.-position+inner_edge[i],inner_size_X/2.),(-inner_size_X/2.-position-outer_edge[i],-inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(6,(-inner_size_X/2.,-inner_size_X/2.-position + inner_edge[i]),(inner_size_X/2,-inner_size_X/2.-position - outer_edge[i])))

            ##### Rounded corners
            gr_cell.add(gdspy.Round(6, (inner_size_X/2.,inner_size_X/2.), radius, inner_radius=position-inner_edge[i],
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
            gr_cell.add(gdspy.Round(6, (inner_size_X/2.,-inner_size_X/2.), radius, inner_radius=position-inner_edge[i],
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
            gr_cell.add(gdspy.Round(6, (-inner_size_X/2., inner_size_X/2.), radius, inner_radius=position-inner_edge[i],
                          initial_angle=numpy.pi/2.,
                          final_angle=numpy.pi))
            gr_cell.add(gdspy.Round(6, (-inner_size_X/2., -inner_size_X/2.), radius, inner_radius=position-inner_edge[i],
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi/2.))

            #Implant Layer
            ## Doping Layer
            center = (0,0)
            ALinner_width = 15
            ALouter_width = 20
            hiw= ALinner_width/2.0
            dw=doping_width/2.
            radius = position+dw
            ##### Sides
            gr_cell.add(gdspy.Rectangle(6,(inner_size_X/2.+position-dw,-inner_size_X/2.),(inner_size_X/2.+position+dw,inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(6,(inner_size_X/2.,inner_size_X/2.+position - dw),(-inner_size_X/2.,inner_size_X/2.+position+dw)))
            gr_cell.add(gdspy.Rectangle(6,(-inner_size_X/2.-position+dw,inner_size_X/2.),(-inner_size_X/2.-position-dw,-inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(6,(-inner_size_X/2.,-inner_size_X/2.-position + dw),(inner_size_X/2,-inner_size_X/2.-position - dw)))

            ##### Rounded corners
            gr_cell.add(gdspy.Round(6, (inner_size_X/2.,inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
            gr_cell.add(gdspy.Round(6, (inner_size_X/2.,-inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
            gr_cell.add(gdspy.Round(6, (-inner_size_X/2., inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=numpy.pi/2.,
                          final_angle=numpy.pi))
            gr_cell.add(gdspy.Round(6, (-inner_size_X/2., -inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi/2.))
           #Contact Layer
            ## Doping Layer
            center = (0,0)
            ALinner_width = 15
            ALouter_width = 20
            hiw= ALinner_width/2.0
            dw=doping_width/2.
            radius = position+dw
            ##### Sides
            gr_cell.add(gdspy.Rectangle(5,(inner_size_X/2.+position-dw,-inner_size_X/2.),(inner_size_X/2.+position+dw,inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(5,(inner_size_X/2.,inner_size_X/2.+position - dw),(-inner_size_X/2.,inner_size_X/2.+position+dw)))
            gr_cell.add(gdspy.Rectangle(5,(-inner_size_X/2.-position+dw,inner_size_X/2.),(-inner_size_X/2.-position-dw,-inner_size_X/2.)))
            gr_cell.add(gdspy.Rectangle(5,(-inner_size_X/2.,-inner_size_X/2.-position + dw),(inner_size_X/2,-inner_size_X/2.-position - dw)))

            ##### Rounded corners
            gr_cell.add(gdspy.Round(5, (inner_size_X/2.,inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=0,
                          final_angle=numpy.pi / 2.0))
            gr_cell.add(gdspy.Round(5, (inner_size_X/2.,-inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=3*numpy.pi/2.0,
                          final_angle=2*numpy.pi))
            gr_cell.add(gdspy.Round(5, (-inner_size_X/2., inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=numpy.pi/2.,
                          final_angle=numpy.pi))
            gr_cell.add(gdspy.Round(5, (-inner_size_X/2., -inner_size_X/2.), radius, inner_radius=position-dw,
                          initial_angle=numpy.pi,
                          final_angle=3.0*numpy.pi/2.))

            #Passivation Opening
            #Ground Ring bump contact`
            if i==0 : 
                gr_cell.add(gdspy.Round(15, (inner_size_X/2.+position,+inner_size_X/6.), bump_radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=2*numpy.pi))
                gr_cell.add(gdspy.Round(15, (inner_size_X/2.+position,-inner_size_X/6.), bump_radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=2*numpy.pi))
                gr_cell.add(gdspy.Round(15, (-inner_size_X/2.-position,inner_size_X/6.), bump_radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=2*numpy.pi))
                gr_cell.add(gdspy.Round(15, (-inner_size_X/2.-position,-inner_size_X/6.), bump_radius, inner_radius=0,
                          initial_angle=0,
                          final_angle=2*numpy.pi))
            #Probing Opening
            opw=0.1*(outer_edge[i]+inner_edge[i])
            gr_cell.add(gdspy.Rectangle(15,(inner_size_X/2.+ position - inner_edge[i] + opw,-inner_size_X/2.),(inner_size_X/2.+ position + outer_edge[i]-opw,- inner_size_X/2.+ 500.)))
        print"doneGR"
        return gr_cell

            
npixX = 256
npixY = 257
pitchX = 55
pitchY = 55
edge = 20


#CLICPix
al_inner = 13
al_outer = 15

imp_inner = 13
imp_outer = 17

ni_inner = 13
ni_outer = 19

UBM_radius = 19.0/2

po_radius = 12.5/2
contact_radius = 10/2


#Timepix3
metal_radius=20
imp_radius=15
contact_radius=7.5
po_radius=15


GenerateRoundPixel(pitchX,pitchY,metal_radius,imp_radius,contact_radius,po_radius)
#GenerateSquarePixel(pitchX,pitchY,al_inner,al_outer,imp_inner,imp_outer,ni_inner,ni_outer,po_radius,contact_radius,UBM_radius,'PIXEL')
#GenerateGuardRings(npixX*pitchX,npixY*pitchY, [0], [5], [5], 3., cellname='GR',3)
GenerateEdge(pitchX,pitchY,npixX,npixY,edge-(pitchX/2.-imp_radius),50)
GeneratePixelArray('PIXEL','EDGE',npixX,npixY,pitchX,pitchY,'TOP')

# Save GDSII to File 
name = os.path.abspath(os.path.dirname(os.sys.argv[0])) + os.sep +\
       'Timepix3_%ix%i_ADVACAM2014_%ium_edges_v2'%(npixX,npixY,edge)
gdspy.gds_print(name + '.gds', unit=1.0e-6, precision=1.0e-9)
print('Sample gds file saved: ' + name + '.gds')
