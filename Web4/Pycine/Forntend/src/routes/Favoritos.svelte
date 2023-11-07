<script>
    let promise = getFavorites();
    
    async function getFavorites() {
        // Faça a solicitação para o serviço TMDB
        const apiKey = '6f77cb8794e999fed44476c8b3303723'; // Substitua por sua chave de API TMDB
        const tmdbURL = `https://api.themoviedb.org/3/movie/popular?api_key=${apiKey}`;
        
        const res = await fetch(tmdbURL);
        
        if (res.ok) {
            const data = await res.json();
            return data.results; // Supondo que os favoritos estejam nos resultados
        } else {
            throw new Error('Falha ao obter dados do TMDB');
        }
    }

    function handleClick() {
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