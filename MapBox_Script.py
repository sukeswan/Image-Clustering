import json
import mapbox
from pprint import pprint
from PIL import Image

MAPBOX_ACCESS_TOKEN = "sk.eyJ1Ijoiamltd2hpdGVoZWFkdWNzYyIsImEiOiJjazJsMnJ4NjQwMnJwM2dxc2t3MHBtZHUzIn0.jOB6E8DYBG5IlZeObq7xyQ"

"""
    Retrieve a satellite map image centered at lat, long
    Returns an HTTP result object, where the retrieved image is located in _content
"""
def get_map_image(lat, long):
    res = mapbox.StaticStyle(access_token=MAPBOX_ACCESS_TOKEN).image(
        username='mapbox', style_id='satellite-v9', lat=lat, lon=long, zoom=19)
    return res

"""
    Retrieve a building areas map image centered at lat, long
    Returns an HTTP result object, where the retrieved image is located in _content
    Depends on the only-buildings-copy style, which was created in mapbox style editor
"""

def get_building_areas_image(lat, long):
    res = mapbox.StaticStyle(access_token=MAPBOX_ACCESS_TOKEN).image(
        username='jimwhiteheaducsc', style_id='ck1wjiell0iru1crquvcgkswj', lat=lat, lon=long, zoom=19)
    return res

"""
    Write the content of the HTTP response into the specified file
"""
def write_res_image_to_file(res, fname):
    newFile = open(fname, "wb")
    newFile.write(res._content)

"""
Retrieve satellite map image for lat,long and write to file
at location path+file
"""
def retrieve_and_save_map_image(lat, long, fname):
    http_result = get_map_image(lat, long)
    if http_result.status_code == 200:
        write_res_image_to_file(http_result, fname)
        print("[Success] ({},{}) written to {}".format(lat, long, fname))
    else:
        print("[Error] ({},{}) || HTTP Status Code: {}".
              format(lat,long,http_result.status_code))

"""
Retrieve building area images for lat,long and write to file
 at location fname
"""
def retrieve_and_save_building_image(lat,long,fname):
    http_result = get_building_areas_image(lat, long)
    if http_result.status_code == 200:
        write_res_image_to_file(http_result, fname)
        print("[Success] ({},{}) written to {}".format(lat, long, fname))
    else:
        print("[Error] ({},{}) || HTTP Status Code: {}".
              format(lat,long,http_result.status_code))

"""
Blend together satellite and building area images
"""
def blend_sat_and_building_images(sat_fname, bldg_fname, merge_fname):
    sat_image = Image.open(sat_fname)
    sat_image_rgba = sat_image.convert("RGBA")

    building_image = Image.open(bldg_fname)
    building_image_rgba = building_image.convert("RGBA")

    merge_image = Image.blend(sat_image_rgba,building_image_rgba, 0.5)

    merge_image.save(merge_fname)


if __name__ == "__main__":
    sc_intersection_list = [(36.968134, -122.043054),
                         (36.967664, -122.042171),
                         (36.967157, -122.041230),
                         (36.966629, -122.040319),
                         (36.969343, -122.041831),
                         (36.969532, -122.041643)]

    # intersections in San Jose, California
    intersection_list = [(37.324063, -121.881590),  # S 1st and E Virginia
                         (37.324581, -121.880515),  # S 2nd and E Virginia
                         (37.325065, -121.879478),  # S 3rd and E Virginia
                         (37.326077, -121.877325),  # S 5th and E Virginia
                         (37.325825, -121.880045),  # S 3rd and Patterson
                         (37.324353, -121.878945),  # S 3rd and Lewis
                         (37.324630, -121.876230),  # S 5th and Martha
                         (37.328572, -121.884912),  # S 1st and E William
                         (37.329067, -121.883855),  # S 2nd and E William
                         (37.329571, -121.882814),  # S 3rd and E William
                         (37.330108, -121.881730)  # S 4th and E William
                         ]
    sanfran_list = [(37.762692, -122.435218),
                    (37.764003, -122.436558),
                    (37.761432, -122.439441),
                    (37.762219, -122.439646),
                    (37.763340, -122.443714),
                    (37.764680, -122.443211),
                    (37.765359, -122.443421),
                    (37.763072, -122.445488),
                    (37.761783, -122.446816),
                    (37.759642, -122.449415),
                    (37.747009, -122.444860),
                    (37.746463, -122.447799),
                    (37.745573, -122.451720),
                    (37.746813, -122.458751),
                    (37.743763, -122.463715),
                    (37.790886, -122.425832),
                    (37.793070, -122.461447),
                    (37.803523, -122.467754),
                    (37.804438, -122.475687),
                    (37.787506, -122.489665),
                    (37.743882, -122.461017),
                    (37.745994, -122.461925),
                    (37.746397, -122.464206),
                    (37.744947, -122.466261),
                    (37.743947, -122.472553),
                    (37.724146, -122.468651),
                    (37.726801, -122.471101),
                    (37.726815, -122.471107),
                    (37.757428, -122.412400),
                    (37.761300, -122.428404),
                    (37.746772, -122.443968),
                    (37.745548, -122.451734),
                    (37.746077, -122.454617),
                    (37.746987, -122.454798),
                    (37.756012, -122.478763),
                    (37.734280, -122.485963),
                    (37.788487, -122.394288),
                    (37.797878, -122.406684),
                    (37.799519, -122.409035),
                    (37.806579, -122.413810),
                    (37.770354, -122.436878),
                    (37.765939, -122.442653),
                    (37.785106, -122.447684),
                    (37.786165, -122.449965),
                    (37.788267, -122.460282),
                    (37.761898, -122.437303),
                    (37.802004, -122.419641),
                    (37.807300, -122.415626),
                    (37.775175, -122.419280),
                    (37.777295, -122.419711)

                    ]
    # for intersection in intersection_list:
    #     path = "sat-photos/"
    #     file = "sat-{}_{}.png".format(intersection[0],intersection[1])
    #     sat_fname = path+file
    #     bldg_fname = path+'b_'+file
    #     merge_fname = path+'m_'+file
    #     retrieve_and_save_map_image(intersection[0], intersection[1], sat_fname)
    #     retrieve_and_save_building_image(intersection[0], intersection[1], bldg_fname)
    #     blend_sat_and_building_images(sat_fname, bldg_fname, merge_fname)
    for intersection in sanfran_list:
        path = "newer-sf/"
        file = "sat-{}_{}.png".format(intersection[0],intersection[1])
        sat_fname = path+file
        bldg_fname = path+'b_'+file
        merge_fname = path+'m_'+file
        retrieve_and_save_map_image(intersection[0], intersection[1], sat_fname)
        retrieve_and_save_building_image(intersection[0], intersection[1], bldg_fname)
        blend_sat_and_building_images(sat_fname, bldg_fname, merge_fname)
