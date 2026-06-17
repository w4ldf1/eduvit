import { configureStore } from "@reduxjs/toolkit";
import postsReducer from "./usersPostsSlice.js";

export const store = configureStore({
  reducer: {
    usersPosts: postsReducer
  }
});
