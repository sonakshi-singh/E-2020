import s3 from './config.js'

async function getImage(filepath){
    var params = {
        Bucket: "beneimages", 
        Key: filepath
    };
    const data = await s3.getObject(params).promise().then(function(result){
        return result
    })
    return data
}

export default getImage
