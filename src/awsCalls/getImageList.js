import getImage from './getImage'

async function getImageList(pathlist){
    var listLength = pathlist.length;
    var imageList = []
    var im
    for (var i = 0; i < listLength; i++){
       im = await getImage(pathlist[i])
       console.log(im)
       if (im){
           imageList.push(im)
       }
    }
    return imageList
}

export default getImageList