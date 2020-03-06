<template>
  <div class="ratingBox">
    <p align="left">
      <img :src="A"/>
      <img :src="B"/>
    </p>
  </div>
</template>

<script>
export default {
    name: 'Outlets',
    props: ["outlets"],
    data(){
        return {
            A: "https://www.worldstandards.eu/wp-content/uploads/electricity-tiles-type-A-200-px.jpg",
            B: "https://www.worldstandards.eu/wp-content/uploads/electricity-tiles-type-B-200-px.jpg",
            C: "https://www.worldstandards.eu/wp-content/uploads/electricity-tiles-type-C-200-px.jpg",
            D: "https://www.worldstandards.eu/wp-content/uploads/electricity-tiles-type-D-200-px.jpg"
        }
    } 
}
</script>