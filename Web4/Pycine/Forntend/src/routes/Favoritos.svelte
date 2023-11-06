<script>
    let promise = getFavorites();
    async function getFavorites(){
        const res = fetch('http://localhost:8000/favorites')
        const text = await res.json();
        if(res.ok){
            return text;
        }else{
            throw new Error(text);
        }
    }

    function handleClick(){
        promise = getFavorites();
    }
</script>
<div class="content FlexCenter">
    <button on:click={handleClick}> Get Favorites </button>
    {#await promise}
        <p>...waiting</p>
    {:then favorites}
        <h1>Lista de Favoritos</h1>
    {#each favorites as favorite}
        <div>
            <p>
                <span>ID: </span>
                {favorite.id}
            </p>

            <p>
                <span>Title: </span>
                {favorite.title}
            </p>
        </div>
    {/each}
    {/await}
</div>

  <style>

  </style>
