<template>
  <div class="detail-container" v-if="post">
    <div class="post-header">
      <span class="movie-badge">🎬 {{ post.movieTitle }}</span>
      <h1>{{ post.title }}</h1>
      <div class="author-info">
        <span>작성자: <strong>{{ post.author }}</strong></span>
        <button @click="openMessageModal" class="btn-msg">쪽지 보내기 ✉️</button>
      </div>
      <p class="date">{{ post.date }}</p>
    </div>

    <div class="post-content">
      {{ post.content }}
    </div>

    <hr />

    <div class="comments-section">
      <h3>댓글 ({{ comments.length }})</h3>
      
      <ul>
        <li v-for="comment in comments" :key="comment.id" class="comment-item">
          <strong>{{ comment.user }}</strong>: {{ comment.text }}
        </li>
      </ul>

      <div class="comment-form">
        <input 
          v-model="newComment" 
          @keyup.enter="addComment" 
          type="text" 
          placeholder="댓글을 입력하세요..." 
        />
        <button @click="addComment">등록</button>
      </div>
    </div>

    <div v-if="showModal" class="modal-overlay" @click.self="showModal = false">
      <div class="modal-content">
        <h3>{{ post.author }}님에게 쪽지</h3>
        <textarea v-model="messageContent" placeholder="내용을 입력하세요"></textarea>
        <div class="modal-actions">
          <button @click="sendMessage">보내기</button>
          <button @click="showModal = false" class="close">취소</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const showModal = ref(false);
const messageContent = ref('');
const newComment = ref('');

// 임시 게시글 데이터
const post = ref<any>(null);
const comments = ref([
  { id: 1, user: '지나가던행인', text: '저도 그 장면 진짜 좋았어요!' },
  { id: 2, user: '평론가지망생', text: '해석이 흥미롭네요.' },
]);

// 페이지 로드 시 데이터 가져오기 (백엔드 연동 시 axios.get 사용)
onMounted(() => {
  // const postId = route.params.id; 
  post.value = {
    id: 1,
    movieTitle: '인셉션',
    title: '마지막 팽이 장면 어떻게 생각하세요?',
    author: '영화광',
    date: '2024-05-20',
    content: '팽이가 멈추는지 안 멈추는지 열린 결말이라 너무 궁금합니다. 여러분의 생각은 어떠신가요?'
  };
});

// 댓글 등록 로직
const addComment = () => {
  if (!newComment.value.trim()) return;
  comments.value.push({
    id: Date.now(),
    user: '나(현재유저)', // 실제로는 로그인한 유저 정보
    text: newComment.value
  });
  newComment.value = '';
};

// 쪽지 모달 열기
const openMessageModal = () => {
  showModal.value = true;
};

// 쪽지 전송 로직
const sendMessage = () => {
  if (!messageContent.value.trim()) return;
  
  // 백엔드로 쪽지 전송 API 호출 (axios.post)
  console.log(`To: ${post.value.author}, Message: ${messageContent.value}`);
  
  alert('쪽지를 보냈습니다!');
  messageContent.value = '';
  showModal.value = false;
};
</script>

<style scoped>
.detail-container { max-width: 800px; margin: 0 auto; padding: 20px; }
.post-header { margin-bottom: 30px; }
.movie-badge { background: #eee; padding: 5px 10px; border-radius: 15px; font-size: 0.8rem; }
.author-info { margin: 10px 0; display: flex; align-items: center; gap: 10px; }
.btn-msg { font-size: 0.8rem; padding: 5px 10px; cursor: pointer; border: 1px solid #ddd; background: white; border-radius: 4px; }
.post-content { min-height: 200px; line-height: 1.6; }

/* 댓글 스타일 */
.comments-section { margin-top: 30px; }
.comment-item { padding: 10px 0; border-bottom: 1px solid #eee; list-style: none; }
.comment-form { display: flex; gap: 10px; margin-top: 20px; }
.comment-form input { flex: 1; padding: 10px; }

/* 모달 스타일 */
.modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); display: flex; justify-content: center; align-items: center; }
.modal-content { background: white; padding: 20px; border-radius: 8px; width: 400px; }
.modal-content textarea { width: 100%; height: 100px; margin: 10px 0; }
.modal-actions { display: flex; gap: 10px; justify-content: flex-end; }
</style>