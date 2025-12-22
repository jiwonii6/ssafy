<template>
  <div class="create-container">
    <h2>새 글 작성</h2>
    
    <form @submit.prevent="submitPost">
      <div class="form-group">
        <label>이야기할 영화 선택</label>
        <select v-model="selectedMovie" required>
          <option disabled value="">영화를 선택해주세요</option>
          <option v-for="movie in movieList" :key="movie.id" :value="movie.title">
            {{ movie.title }}
          </option>
        </select>
      </div>

      <div class="form-group">
        <label>제목</label>
        <input v-model="title" type="text" placeholder="제목을 입력하세요" required />
      </div>

      <div class="form-group">
        <label>내용</label>
        <textarea v-model="content" rows="10" placeholder="자유롭게 이야기해주세요" required></textarea>
      </div>

      <button type="submit" class="btn-submit">등록하기</button>
    </form>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// 영화 데이터 (실제로는 API로 검색 기능을 구현해야 함)
const movieList = ref([
  { id: 101, title: '인셉션' },
  { id: 102, title: '인터스텔라' },
  { id: 103, title: '범죄도시4' },
  { id: 104, title: '파묘' },
]);

const selectedMovie = ref('');
const title = ref('');
const content = ref('');

const submitPost = () => {
  // 여기에 백엔드(Django)로 데이터를 보내는 로직이 들어갑니다 (axios.post 등)
  const postData = {
    movie: selectedMovie.value,
    title: title.value,
    content: content.value
  };
  
  console.log('전송할 데이터:', postData);
  alert('게시글이 등록되었습니다!');
  router.push({ name: 'Community' }); // 목록으로 이동
};
</script>

<style scoped>
.create-container { max-width: 800px; margin: 0 auto; padding: 20px; }
.form-group { margin-bottom: 20px; display: flex; flex-direction: column; }
.form-group label { margin-bottom: 8px; font-weight: bold; }
input, select, textarea { padding: 10px; border: 1px solid #ddd; border-radius: 4px; }
.btn-submit { width: 100%; padding: 15px; background-color: #3b82f6; color: white; border: none; border-radius: 5px; font-size: 1rem; cursor: pointer; }
</style>