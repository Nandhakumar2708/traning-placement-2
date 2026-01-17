class Solution {
    public static ListNode oddEvenList(ListNode head) {

      if (head == null || head.next == null) {
        return head;
      }

      ListNode odd = head;
      ListNode even = head.next;
      ListNode evenHead = head.next;

      while (even != null && even.next != null) {
        odd.next = even.next;
        odd = odd.next;

        even.next = odd.next;
        even = even.next;
      }
      odd.next = evenHead;
      return head;
    }

    public static ListNode arrayToLL(int[] arr){
      if (arr.length ==0) {
        return null;
      }
      ListNode head = new ListNode(arr[0]);
      ListNode tail = head;
      for (int i = 1; i < arr.length; i++) {
        ListNode newNode = new ListNode(arr[i]);
        tail.next = newNode;
        tail = newNode;
      }
      return head;
    }

    public static void main(String[] args) {
      int[] arr = {2,5,8,9,1,2,5};
      ListNode head = arrayToLL(arr);
      head = oddEvenList(head);
      while (head != null) {
        System.out.print(head.val + " ");
        head = head.next;
      }
    }
}
