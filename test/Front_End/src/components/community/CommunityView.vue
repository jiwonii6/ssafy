<template>
  <div class="community-container">
    <div class="header">
      <h1>🎬 영화 수다방</h1>
      <button @click="goToCreate" class="btn-write">글쓰기</button>
    </div>

    <div class="post-list">
      <div 
        v-for="post in posts" 
        :key="post.id" 
        class="post-item"
        @click="goToDetail(post.id)"
      >
        <div class="movie-tag">🍿 {{ post.movieTitle }}</div>
        <h3 class="post-title">{{ post.title }}</h3>
        <div class="post-meta">
          <span>작성자: {{ post.author }}</span>
          <span>{{ post.date }}</span>
          <span>댓글 {{ post.commentCount }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// 임시 데이터 (나중에 백엔드에서 가져올 데이터)
const posts = ref([
  { id: 1, movieTitle: '인셉션', title: '마지막 팽이 장면 어떻게 생각하세요?', author: '영화광', date: '2024-05-20', commentCount: 5 },
  { id: 2, movieTitle: '범죄도시4', title: '이번 액션 진짜 시원하네요 ㅋㅋ', author: '팝콘러', date: '2024-05-21', commentCount: 12 },
]);

const goToCreate = () => {
  router.push({ name: 'PostCreate' });
};

const goToDetail = (id: number) => {
  router.push({ name: 'PostDetail', params: { id } });
};
</script>

<style scoped>
.community-container { max-width: 800px; margin: 0 auto; padding: 20px; }
.header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
.btn-write { background-color: #ff4081; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
.post-item { border-bottom: 1px solid #eee; padding: 15px 0; cursor: pointer; transition: background 0.2s; }
.post-item:hover { background-color: #f9f9f9; }
.movie-tag { color: #666; font-size: 0.9rem; margin-bottom: 5px; }
.post-title { margin: 5px 0; font-size: 1.2rem; }
.post-meta { font-size: 0.8rem; color: #999; display: flex; gap: 10px; }
</style>