<template>
  <div class="ratingBox">
    <h3 align="left"><b>Safety Rating</b></h3>
    <p align="left">
      <b>{{getCountryID()}}{{rating}}</b>
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
            allRatings:[]
        }
    },
    methods: {
      getRatings: async function() {
        var Feed = require('rss-to-json');
        var self = this;
        Feed.load('https://cors-anywhere.herokuapp.com/https://travel.state.gov/_res/rss/TAsTWs.xml', function(err, rss){
           var countryList = rss.items;
           self.allRatings = countryList;
         });
        //response.then(()=>{return 1});
      },
      getCountryID :  function() {
        var len = this.$props.country.length;
        for (var i=0; i<this.allRatings.length; i++){
             if (this.allRatings[i].title.substring(0,len) == this.$props.country){
               this.countryID = i;
               console.log(i);
             }
           }
        if (this.countryID>=0){
             this.rating = this.allRatings[this.countryID].title;
             }
      }
    },
    mounted: function() {
      this.getRatings();
    } 
}
</script>