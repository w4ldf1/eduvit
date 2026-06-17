import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { changeSortDirection, loadUsersPosts, selectUser, setSearch } from "./usersPostsSlice.js";

function App() {
  const dispatch = useDispatch();
  const { users, posts, selectedUserId, search, sortDirection, status, error } = useSelector(state => state.usersPosts);

  useEffect(() => {
    dispatch(loadUsersPosts());
  }, [dispatch]);

  const normalizedSearch = search.trim().toLowerCase();
  const filteredUsers = users.filter(user => {
    return (
      user.name.toLowerCase().includes(normalizedSearch) ||
      user.username.toLowerCase().includes(normalizedSearch) ||
      user.email.toLowerCase().includes(normalizedSearch)
    );
  });
  const selectedUser = users.find(user => user.id === selectedUserId);
  const userPosts = posts
    .filter(post => post.userId === selectedUserId)
    .sort((firstPost, secondPost) => {
      if (sortDirection === "asc") {
        return firstPost.id - secondPost.id;
      }

      return secondPost.id - firstPost.id;
    });

  return (
    <main className="page">
      <section className="top-panel">
        <div>
          <p className="eyebrow">JSONPlaceholder</p>
          <h1>Пользователи и посты</h1>
        </div>
        <div className="toolbar">
          <input
            type="search"
            value={search}
            onChange={event => dispatch(setSearch(event.target.value))}
            placeholder="Поиск пользователя"
          />
          <button type="button" onClick={() => dispatch(changeSortDirection())}>
            Сортировка: {sortDirection === "asc" ? "1-10" : "10-1"}
          </button>
        </div>
      </section>

      {status === "loading" && <p className="status">Загрузка данных...</p>}
      {status === "failed" && <p className="status error">{error}</p>}

      {status === "succeeded" && (
        <section className="workspace">
          <aside className="users-list">
            {filteredUsers.map(user => (
              <button
                key={user.id}
                type="button"
                className={user.id === selectedUserId ? "user active" : "user"}
                onClick={() => dispatch(selectUser(user.id))}
              >
                <span>{user.name}</span>
                <small>{user.email}</small>
              </button>
            ))}
          </aside>

          <section className="posts-area">
            <div className="posts-header">
              <div>
                <p className="eyebrow">Автор</p>
                <h2>{selectedUser?.name}</h2>
              </div>
              <span>{userPosts.length} постов</span>
            </div>

            <div className="posts-grid">
              {userPosts.map(post => (
                <article key={post.id} className="post-card">
                  <header>{selectedUser?.name}</header>
                  <h3>{post.title}</h3>
                  <p>{post.body}</p>
                </article>
              ))}
            </div>
          </section>
        </section>
      )}
    </main>
  );
}

export default App;
