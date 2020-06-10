    console.log("yeh import hua re");

    function getUniqueId() {
        return 'private-' + Math.random().toString(36).substr(2, 9);
      }
    
      // function to get a query param's value
      function getUrlParameter(name) {
        name = name.replace(/[\[]/, '\\[').replace(/[\]]/, '\\]');
        var regex = new RegExp('[\\?&]' + name + '=([^&#]*)');
        var results = regex.exec(location.search);
        return results === null ? '' : decodeURIComponent(results[1].replace(/\+/g, ' '));
      }

    export const collabFunctions = {
   ChangeID: function(){
    var doc=document.querySelector("textarea");
    console.log(doc.innerHTML);
    // doc.innerHTML="test123443"
    console.log("yeh bhi chala");    
    var id = getUrlParameter('id');
        if (!id) {
        location.search = location.search
            ? '&id=' + getUniqueId() : 'id=' + getUniqueId();
        //   return;
        }
    console.log("id was found",id);
    var pusher = new Pusher("1016331",{
        cluster: "us2"});
        console.log("pusher val",pusher);
        var channel = pusher.subscribe(id);
        console.log("channel val",channel);
        console.log(channel.bind("client-text-edit"));  
        channel.bind('client-text-edit', function(html) {
        // save the current position
        console.log("this ran with valye",html)
        doc.value = html;
        });

    function triggerChange (e) {
        console.log(e.target.value);
        console.log("there were changes",e.target.value);
        channel.trigger('client-text-edit', e.target.value);
        // channel.trigger('client-text-edit', e.target.value);
        console.log("channe",channel.trigger('client-text-edit',e.target.value))
        
    }
    doc.addEventListener('input', triggerChange); 

            

    },

    
    }

// export default{
//     name:"pepsicolalollipop"
// }

// export default changeID;