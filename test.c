#include <stdio.h>
int main(void)
{
    int num;
    float major = 0.0, culture = 0.0;
    
    for(int i = 0; i < 5; i++){
        printf("전공 점수를 입력하세요 : ");
        scanf("%d", &num);
        if (num >= 90) {
            major += 4.5;
        }
        else if (num >= 80) {
            major += 4.0;
        }
        else if (num >= 70) {
            major += 3.5;
        }
        else if (num >= 60) {
            major += 3.0;
        }
    }
    for(int i = 0; i < 2; i++){
        printf("교양 점수를 입력하세요 : ");
        scanf("%d", &num);
        if (num >= 90) {
            culture += 4.5;
        }
        else if (num >= 80) {
            culture += 4.0;
        }
        else if (num >= 70) {
            culture += 3.5;
        }
        else if (num >= 60) {
            culture += 3.0;
        }
    }
    printf("학점 : %.1f\n", (major*3 + culture*2)/19 );
}