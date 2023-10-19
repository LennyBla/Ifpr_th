<script>
    import '../globals.css'
    let promise = "";
    let nameArtist = "";
    async function getArtista(name) {
        // faz um request GET para endpoint /filmes
        const res = await fetch(`http://localhost:8000/artistas/${name}`);
        const text = await res.json();
        if (res.ok) {
            return text;
        } else {
            throw new Error(text);
        }
    }
    function handleClick() {
        return (promise = getArtista(nameArtist));
    }
</script>

<div class="content flexCenter">
    <h1>Lista de Artistas</h1>
    <form action="">
        <input bind:value={nameArtist} type="text" />
        <button on:click={handleClick}> Get Artistas </button>
    </form>

    {#await promise}
        <p>...waiting</p>
    {:then artistas}
        {#each artistas as artista}
        <div class="artist boxBorder flexCenter">
            <p>{artista.id}</p>
            <p>{artista.name}</p>
            <img
                src="https://image.tmdb.org/t/p/w185/{artista.profile_path}"
                alt=""
            />
            <p>{artista.biography}</p>
        </div>
        {/each}
    {:catch error}
        <p style="color: red">{error.message}</p>
    {/await}
</div>
<style>
.content, .artist {
    display: flex;
    flex-direction: column;
}

.artist {
    width: 60%;
    margin: 0 auto;
    padding: 1rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
</style>