import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

export const loadUsersPosts = createAsyncThunk("usersPosts/loadUsersPosts", async () => {
  const [usersResponse, postsResponse] = await Promise.all([
    fetch("https://jsonplaceholder.typicode.com/users"),
    fetch("https://jsonplaceholder.typicode.com/posts")
  ]);

  if (!usersResponse.ok || !postsResponse.ok) {
    throw new Error("Не удалось загрузить данные");
  }

  const users = await usersResponse.json();
  const posts = await postsResponse.json();

  return { users, posts };
});

const usersPostsSlice = createSlice({
  name: "usersPosts",
  initialState: {
    users: [],
    posts: [],
    selectedUserId: null,
    search: "",
    sortDirection: "asc",
    status: "idle",
    error: ""
  },
  reducers: {
    selectUser(state, action) {
      state.selectedUserId = action.payload;
    },
    setSearch(state, action) {
      state.search = action.payload;
    },
    changeSortDirection(state) {
      state.sortDirection = state.sortDirection === "asc" ? "desc" : "asc";
    }
  },
  extraReducers: builder => {
    builder
      .addCase(loadUsersPosts.pending, state => {
        state.status = "loading";
        state.error = "";
      })
      .addCase(loadUsersPosts.fulfilled, (state, action) => {
        state.status = "succeeded";
        state.users = action.payload.users;
        state.posts = action.payload.posts;
        state.selectedUserId = action.payload.users[0]?.id ?? null;
      })
      .addCase(loadUsersPosts.rejected, (state, action) => {
        state.status = "failed";
        state.error = action.error.message;
      });
  }
});

export const { selectUser, setSearch, changeSortDirection } = usersPostsSlice.actions;
export default usersPostsSlice.reducer;
