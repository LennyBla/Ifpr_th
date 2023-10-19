<script>
    import Home from "./Home.svelte";   
    import Artista from "./Artista.svelte";
	import Movie from "./Movie.svelte";
	import Nav from "./Nav.svelte";
	import User from "./User.svelte";
    import UserList from "./UserList.svelte";
	import Sobre from "./Sobre.svelte";   
    let menu = 1; // Defina o valor inicial do menu

    function switchPage(page) {
        menu = page;
    }
</script>
<nav class="menu-horizontal">

    <div class="components-nav">
      <ul>
          <li><a href="/" on:click|preventDefault={() => (menu = 1)}>Home</a></li>
          <li><a href="/" on:click|preventDefault={() => (menu = 2)}>Movie</a></li>
          <li><a href="/" on:click|preventDefault={() => (menu = 3)}>Artist</a></li>
          <li><a href="/" on:click|preventDefault={() => (menu = 4)}>User</a></li>
          <li><a href="/" on:click|preventDefault={() => (menu = 5)}>User List</a></li>
          <li><a href="/" on:click|preventDefault={() => (menu = 6)}>Sobre</a></li>
      </ul>
    </div>
  </nav>

<Nav bind:menu={menu} />

{#if menu === 1}
    <Home />

{:else if menu === 2}
    <Movie/>

{:else if menu === 3}
    <Artista />

{:else if menu === 4}
    <User />
    
{:else if menu === 5}
    <UserList />

{:else if menu === 6}
    <Sobre/>
{/if}

<style>
    nav.menu-horizontal {
  background-color: #000000c6; /* Cor de fundo do menu */
  color: #fff; /* Cor do texto */
  padding: 8px; /* Espaçamento interno */
  display: flex; /* Torna os itens do menu flexíveis */
  justify-content: flex-end; /* Alinha os itens à direita */
  box-shadow: 0px 1px 5px #373737;
  align-items: center; /* Alinha os itens verticalmente */
}

nav.menu-horizontal ul {
  list-style: none; /* Remove marcadores de lista */
  display: flex; /* Torna os itens da lista flexíveis */
}

nav.menu-horizontal ul li {
  margin-left: 30px; /* Espaço entre os itens do menu (à direita) */
}

nav.menu-horizontal a {
  text-decoration: none; /* Remove sublinhado dos links */
  color: #fff; /* Cor dos links */
  font-weight: 300; /* Peso da fonte */
}

</style>