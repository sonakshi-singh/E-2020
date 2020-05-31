import getImage from './getImage'

function getImageList(pathlist){
    var listLength = pathlist.length;
    var imageList = []
    var im
    for (var i = 0; i < listLength; i++){
       im = getImage(pathlist[i])
       if (im){
           imageList.append(im)
       }
    }
    return imageList
}

export default getImageList