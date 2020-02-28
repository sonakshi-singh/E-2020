<template>
  <div class="ratingBox">
    <h3 align="left"><b>Safety Rating</b></h3>
    <p align="left">
      <b>{{getCountryID()}}{{rating}}</b>
      <br/>{{message}}
    </p>
  </div>
</template>

<script>
export default {
    name: 'SafetyRating',
    props: ["country"],
    data(){
        return {
            rating:"Loading...",
            countryID:-1,
            allRatings:[],
            message: ""
        }
    },
    methods: {
      getRatings: async function() {
        var Feed = require('rss-to-json');
        var self = this;
        Feed.load('https://cors-anywhere.herokuapp.com/https://travel.state.gov/_res/rss/TAsTWs.xml', function(err, rss){
           var countryList = rss.items;
           self.allRatings = countryList;
           console.log(countryList);
         });
        //response.then(()=>{return 1});
      },
      getCountryID :  function() {
        var len = this.$props.country.length;
        for (var i=0; i<this.allRatings.length; i++){
             if (this.allRatings[i].title.substring(0,len) == this.$props.country){
               this.countryID = i;
             }
           }
        if (this.countryID>=0){
             this.rating = this.allRatings[this.countryID].title;
             console.log(this.allRatings[this.countryID]);
             this.message = this.stripHtml(this.allRatings[this.countryID].description);
             }
      },
      stripHtml : function (html){
        // Create a new div element
        var temporalDivElement = document.createElement("div");
        // Set the HTML content with the providen
        temporalDivElement.innerHTML = html;
        // Retrieve the text property of the element (cross-browser support)
        return temporalDivElement.textContent || temporalDivElement.innerText || "";
      }
    },
    mounted: function() {
      this.getRatings();
    } 
}
</script>