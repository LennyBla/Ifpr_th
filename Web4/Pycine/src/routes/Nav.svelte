<script>
  export let menu;
</script>

<div id="componente-nav">
  
  <ul>
    <li>
      <a href="/" on:click|preventDefault={() => (menu = 1)}>Movie</a>
      <a href="/" on:click|preventDefault={() => (menu = 2)}>Artist</a>
      <a href="/" on:click|preventDefault={() => (menu = 3)}>Users</a>
    </li>
  </ul>
  
</div>
<style>
  ul {
    color: red;
  }
  li {
    display: inline-block;
  }
</style>