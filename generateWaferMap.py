#!/usr/bin/python
import os
import numpy
import gdspy

ld_mask_edge = {'layer': 300, 'datatype': 0}
ld_kerf = {'layer': 200, 'datatype': 0}
ld_acfmask = {'layer': 100, 'datatype': 0}
ld_topmetal= {'layer': 81, 'datatype': 0}
ld_po= {'layer': 27, 'datatype': 1}


def GenerateCell(chipX = 14100., chipY=16210.,leftKerf=85.,rightKerf=15.,topKerf=465.,botKerf=15.,narray_X=13,narray_Y=11,mask_width=254000.,wafer_offset_x=-570.0,wafer_offset_y=2595.0,wafer_radius=100000) :

    #Extract existing die mask top cell from GDS
    gdsii = gdspy.current_library.read_gds(infile='Timepix3_top_ACF_Nometal.GDS',layers=ld_acfmask)
    die =  gdspy.current_library.extract("Timepix3_top")
    die_ref = gdspy.CellReference(die,origin=(leftKerf,botKerf))

    #Create top reticle cell
    pixel_cell = gdspy.Cell("Reticle_top")

    # Create a kerf layer for visualization
    kerfWidth  = leftKerf+rightKerf+chipX
    kerfHeight = topKerf+botKerf+chipY
    Kerf = gdspy.Rectangle((0,0), (kerfWidth, kerfHeight),**ld_kerf)

   # Add cells to the top cell
    pixel_cell.add(Kerf)
    pixel_cell.add(die_ref.get_polygonsets())
    pixel_cell.add(die_ref.get_paths())
    #Fill the Kerf with Resist
    pixel_cell.add(gdspy.Rectangle((0,0), (leftKerf, kerfHeight),**ld_acfmask))
    pixel_cell.add(gdspy.Rectangle((0,0), (kerfWidth, botKerf),**ld_acfmask))
    pixel_cell.add(gdspy.Rectangle((0,kerfHeight), (kerfWidth, kerfHeight-topKerf),**ld_acfmask))
    pixel_cell.add(gdspy.Rectangle((kerfWidth-rightKerf,0), (kerfWidth, kerfHeight-topKerf),**ld_acfmask))

    wafer_cell = gdspy.Cell('Wafer_Top')
    mask_edge = gdspy.Rectangle((-mask_width/2,-mask_width/2), (mask_width/2., mask_width/2.),**ld_mask_edge)

    array_origin_x = -narray_X*(leftKerf+rightKerf+chipX)/2. + wafer_offset_x
    array_origin_y = -narray_Y*(botKerf+topKerf+chipY)/2. + wafer_offset_y


    wafer_edge = gdspy.Path(1,(wafer_radius,0))
    wafer_edge.arc(wafer_radius,0,360,layer=400)
    wafer_cell.add(wafer_edge)

    print kerfWidth,kerfHeight
    wafer_cell.add(gdspy.CellArray(pixel_cell,narray_X,narray_Y,spacing=(kerfWidth,kerfHeight),origin=(array_origin_x,array_origin_y)))
    wafer_cell.add(mask_edge)




    # View the resulting cell
    gdspy.LayoutViewer(cells=[wafer_cell],depth=1)


    gdspy.write_gds("wafer_mask.gds",cells=[wafer_cell,pixel_cell])



if __name__ == '__main__':
    GenerateCell()