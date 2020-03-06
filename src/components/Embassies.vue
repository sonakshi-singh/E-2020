<template>
  <div class="ratingBox">
    <p align="left">
      {{closestEmbassy}}
    </p>
  </div>
</template>

<script>
import json from '../../embassies.json'
export default {
    name: 'Embassies',
    props: ["City"],
    data(){
        return {
            embassies: json,
            closestEmbassy: ""
        }
    },
    mounted: function() {
        this.closestEmbassy = this.embassies[0]
    }
      
}
</script>