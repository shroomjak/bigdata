#include <stdio.h>


int main(){
    char key[8];
    long long words, posts;
    long long total_words = 0, total_posts = 0;

    while(scanf("%7s\t%lld\t%lld", key, &words, &posts) == 3){
        total_words += words;
        total_posts += posts;
    }

    if(total_posts > 0){
        printf("posts\t%lld\n", total_posts);
        printf("total_words\t%lld\n", total_words);
        printf("avg_words\t%.1f\n", (double)total_words / total_posts);
    }

    return 0;
}
