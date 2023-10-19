<script>
  export let menu
</script>

  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
<nav class="menu-lateral">

  <div class="btn-expandir">
    <i class="bi bi-list" id = "btn-exp"></i>
  </div>
  <ul>
    <li class="item-menu">
      <a href="#">
        <span class="icon"><i class="bi bi-house"></i></span>
        <li><a class="txt-link" href="/" on:click|preventDefault={() => (menu=1)}>Home</a></li>
      </a>
    </li>
    <li class="item-menu">
      <a href="#">
        <span class="icon"><i class="bi bi-tv"></i></span>
        <li><a class="txt-link" href="/" on:click|preventDefault={() => (menu = 2)}>Movie</a></li>
    
      </a>
    </li>
    <li class="item-menu">
      <a href="#">
        <span class="icon"><i class="bi bi-person-circle"></i></span>
        <li><a class="txt-link" href="/" on:click|preventDefault={() => (menu=3)}>Perfil</a></li>

      </a>
    </li>
    <li class="item-menu">
      <a href="#">
        <span class="icon"><i class="bi bi-box-arrow-left"></i></span>
        <li><a class="txt-link" href="/" on:click|preventDefault={() => (menu=4)}>Sair</a></li>
        
      </a>
    </li>
  </ul>
</nav>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Noto Sans', sans-serif;
  }

  body {
    height: 100vh;
    background-color: #202020;
  }

  nav.menu-lateral {
    width: 60px;
    height: 100%;
    background-color: #000000c3;
    padding: 40px 0 30px -1%;
    box-shadow: 1px 10px 5px #2b2a2ad9;
    position: fixed;
    top: 0;
    left: 0;
    overflow: hidden;
    transition: .4s;
  }
  nav.menu-lateral:hover{
    width: 200px;

  }

  .btn-expandir {
    width: 100%;
    padding: 10px;
  }

  .btn-expandir > i {
    color: #fff;
    font-size: 190%;
    cursor: pointer;
    margin-left: 5px;
    margin-block: 10px;
  }

  ul {
    height: 100%;
    list-style-type: none;
  }

  ul li.item-menu {
    transition: .1s;
  }

  ul li.item-menu:hover {
    background: #343434c5;
  }

  ul li.item-menu a {
    color: #fff;
    text-decoration: none;
    font-size: 20px;
    padding: 20px 4%;
    display: flex;
    margin-bottom: 40px;
    line-height: 0%;
  }

  ul li.item-menu a .txt-link{
    margin-left: 40px;
    
    }

  ul li.item-menu a .icon > i {
    font-size: 30px;
    margin-left: 10px;
  }
</style>