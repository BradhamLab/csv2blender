import sys
import numpy as np

def poor_mans_blender(center):
    """
    Write a line to generate a 3d point for a blender model.

    Arguments:
        center (np.array): xyz-center of interest.
    """
    # need to re-orient centers 
    line = "bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=6, view_align=False, enter_editmode=False, location=({0},{1},{2}), rotation=(0,0,0), layers=(True,False,False,False,False,False,False,False,False, False,False,False,False,False,False,False,False,False,False,False))"
    return line.format(center[0], center[1], center[2])


def center_coordinates(coord_array):
    """
    Center 3D numpy array to origin (0, 0, 0)

    Arguments:
        coord_array (numpy.array): n x 3 numpy array where n is the number of
        cells and columns relate to x, y, z coordinates
    """
    origin_shift = np.mean(coord_array, axis=0)
    return coord_array - origin_shift

def write_blender_script(input_file, output_file):
    data = np.loadtxt(input_file, delimiter=',')
    centered = center_coordinates(data)
    with open(output_file, 'w') as out:
        for i, each in enumerate(centered):
            line = poor_mans_blender(each)
            out.write(line + '\n')

def usage():
    str="This script generates a blender script given a .csv file of PMC centroids\
    \n\n\nThe script takes two files as input, an input file name and an output \
    file name. The input file is expected to be a .csv file, while the output file\
    is expected to be .txt file. To run the script issue the following command:\n\n\n\
    \tpython csv2blender.py <input_file> <output_file>\n\n\n"
    print(str)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
        if args[0].endswith('.csv') and args[1].endswith('.txt'):
            write_blender_script(args[0], args[1])
        else:
            usage()
    else:
        usage()
    # import sys

# filePath = sys.argv[1]

# coordBlock = 0  			#Coordblock designates the desired Blender layer minus 1

# with open(filePath) as f:
#     content = f.readlines()
#     for crudeList in content:
#         coordList = crudeList.split('\r')
#     for xyz in coordList:		#iterate through each line in cvs file, store as variable xyz
# 	if xyz == ',,':			#if the line is blank, increase layer by 1
# 	    coordBlock +=1
# 	else:				#if the line contains xyz coordinates, print each coordinate with respective layer
# 	    varLayer = ["False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False","False"]
# 	    varLayer[coordBlock] = "True"
# 	    layerStr = ','.join(str(layer) for layer in varLayer)
	    
# 	    print "bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, size=0.5, view_align=False, enter_editmode=False, location=(" + xyz + "), rotation=(0,0,0), layers=(" + layerStr + "))"
