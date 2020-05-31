import s3 from './config.js'

async function getImage(filepath){
    var params = {
        Bucket: "beneimages", 
        Key: filepath
    };
    s3.getObject(params, await function (err, data) {
        if (err) {
            return false;
        }
        else {
            return data;
        }
    })
}

export default getImage